from grammar.OOPsyBaseVisitor import OOPsyBaseVisitor
from grammar.OOPsyParser import OOPsyParser


class OOPsyType:
    def __init__(self, base, subtypes=None):
        self.base = base
        self.subtypes = subtypes or []

    def __eq__(self, other):
        return isinstance(other, OOPsyType) and self.base == other.base and self.subtypes == other.subtypes

    def __str__(self):
        if self.subtypes:
            return f"{self.base}<{', '.join(map(str, self.subtypes))}>"
        return self.base

class ClassDef:
    def __init__(self, name, superclass=None, is_abstract=False):
        self.name = name
        self.superclass = superclass
        self.attributes = {}
        self.methods = {}
        self.abstract_methods = set()
        self.is_abstract = is_abstract
        self.variables = {}

    def get_attr(self, name):
        if name in self.attributes:
            return None
        elif self.superclass:
            return self.superclass.get_attr(name)
        else:
            raise Exception(f"Atrybut '{name}' nie istnieje w klasie '{self.name}' ani w jej nadklasie")

    def get_attr_modifier(self, name):
        if name in self.attributes:
            return self.attributes[name][0]
        elif self.superclass:
            return self.superclass.get_attr_modifier(name)
        else:
            return None

    def get_method_modifier(self, name):
        if name in self.methods:
            return self.methods[name][0]
        elif self.superclass:
            return self.superclass.get_method_modifier(name)
        else:
            return None

    def get_all_super_methods(self):
        methods = {}
        if self.superclass:
            methods.update(self.superclass.get_all_super_methods())
            methods.update(self.superclass.methods)
        return methods


class Instance:
    def __init__(self, class_def):
        self.class_def = class_def
        self.fields = {}

    def get_attr(self, name, requester=None):
        if name in self.fields:
            modifier = self.class_def.get_attr_modifier(name)
            if modifier == "private" and requester != self:
                raise Exception(f"Nie można odczytać prywatnego atrybutu '{name}' spoza klasy '{self.class_def.name}'")
            return self.fields[name]

        if name in self.class_def.attributes:
            modifier = self.class_def.get_attr_modifier(name)
            if modifier == "private" and requester != self:
                raise Exception(f"Nie można odczytać prywatnego atrybutu '{name}' spoza klasy '{self.class_def.name}'")
            return None

        if self.class_def.superclass:
            return self.class_def.superclass.get_attr(name, requester)

        raise Exception(f"Brak atrybutu '{name}' w obiekcie '{self.class_def.name}'")

    # def set_attr(self, name, value, requester=None):
    #     if name in self.class_def.attributes:
    #         modifier = self.class_def.get_attr_modifier(name)
    #         if modifier == "private" and requester != self:
    #             raise Exception(
    #                 f"Nie można zmodyfikować prywatnego atrybutu '{name}' spoza klasy '{self.class_def.name}'")
    #         self.fields[name] = value
    #     elif self.class_def.superclass:
    #         self.class_def.superclass.set_attr(name, value, requester)
    #     else:
    #         raise Exception(f"Próba ustawienia nieistniejącego atrybutu '{name}'")
    def set_attr(self, name, value, requester=None):
        if name in self.class_def.attributes:
            modifier = self.class_def.get_attr_modifier(name)
            if modifier == "private" and requester != self:
                raise Exception(
                    f"Nie można zmodyfikować prywatnego atrybutu '{name}' spoza klasy '{self.class_def.name}'")
            self.fields[name] = value
        elif self.class_def.superclass:
            super_instance = Instance(self.class_def.superclass)
            super_instance.fields = self.fields
            super_instance.set_attr(name, value, requester)
        else:
            raise Exception(f"Próba ustawienia nieistniejącego atrybutu '{name}'")

    # Basic version
    # def get_attr(self, name):
    #     if name in self.fields:
    #         return self.fields[name]
    #     elif name in self.class_def.attributes:
    #         return None
    #     elif self.class_def.superclass:
    #         return self.class_def.superclass.get_attr(name)
    #     else:
    #         raise Exception(f"Brak atrybutu '{name}' w obiekcie '{self.class_def.name}'")
    #
    # def set_attr(self, name, value):
    #     if name in self.class_def.attributes or self.class_def.superclass:
    #         self.fields[name] = value
    #     else:
    #         raise Exception(f"Próba ustawienia nieistniejącego atrybutu '{name}'")

class Interpreter(OOPsyBaseVisitor):
    def __init__(self, input_func=input, print_func=print):
        super().__init__()
        self.input_func = input_func
        self.print_func = print_func
        self.classes = {}
        self.variables = {}
        self.current_instance = None

    def visitProgram(self, ctx):
        for child in ctx.classDecl():
            self.visit(child)
        self.visit(ctx.mainMethod())

    def visitClassDecl(self, ctx):
        name = ctx.IDENTIFIER(0).getText()
        superclass = None
        if ctx.INHERITS_KEYWORD():
            superclass_name = ctx.IDENTIFIER(1).getText()
            superclass = self.classes.get(superclass_name)
            if superclass is None:
                raise Exception(f"Brak klasy bazowej '{superclass_name}'")

        is_abstract = bool(ctx.ABSTRACT_KEYWORD())
        class_def = ClassDef(name, superclass, is_abstract)

        for element in ctx.classElement():
            if element.attributeDecl():
                attr_ctx = element.attributeDecl()
                attr_name = attr_ctx.IDENTIFIER().getText()
                modifier = attr_ctx.accessModifier().getText() if attr_ctx.accessModifier() else "public"
                class_def.attributes[attr_name] = (modifier, None)

            elif element.methodDecl():
                method_ctx = element.methodDecl()
                method_name = method_ctx.IDENTIFIER().getText()
                modifier = method_ctx.accessModifier().getText() if method_ctx.accessModifier() else "public"
                is_abstract_method = bool(method_ctx.ABSTRACT_KEYWORD())
                is_override = bool(method_ctx.OVERRIDE_KEYWORD())
                is_final = bool(method_ctx.FINAL_KEYWORD())

                # Pobranie metod z nadklasy
                super_methods = class_def.get_all_super_methods()
                overridden = method_name in super_methods

                if is_override and not overridden:
                    raise Exception(f"Metoda '{method_name}' oznaczona jako override, ale nie istnieje w nadklasie.")

                if overridden:
                    super_modifier, _ = super_methods[method_name]
                    if super_modifier == "final":
                        raise Exception(f"Nie mozna nadpisac finalnej metody '{method_name}'")

                if is_abstract_method:
                    if method_ctx.block():
                        raise Exception(f"Abstrakcyjna metoda '{method_name}' nie może mieć ciała.")
                    class_def.abstract_methods.add(method_name)
                    class_def.methods[method_name] = ("abstract", None)
                else:
                    final_or_modifier = "final" if is_final else modifier
                    class_def.methods[method_name] = (final_or_modifier, method_ctx)

        inherited_abstracts = set()
        if superclass:
            inherited_abstracts |= superclass.abstract_methods

        not_implemented = inherited_abstracts - set(class_def.methods.keys())
        if not_implemented and not is_abstract:
            raise Exception(f"Klasa '{name}' nie implementuje metod abstrakcyjnych: {', '.join(not_implemented)}")

        self.classes[name] = class_def

    # def visitClassDecl(self, ctx):
    #     name = ctx.IDENTIFIER(0).getText()
    #     superclass = None
    #     if ctx.INHERITS_KEYWORD():
    #         superclass_name = ctx.IDENTIFIER(1).getText()
    #         superclass = self.classes.get(superclass_name)
    #         if superclass is None:
    #             raise Exception(f"Brak klasy bazowej '{superclass_name}'")
    #     is_abstract = bool(ctx.ABSTRACT_KEYWORD())
    #     class_def = ClassDef(name, superclass)
    #     for element in ctx.classElement():
    #         if element.attributeDecl():
    #             attr_ctx = element.attributeDecl()
    #             attr_name = attr_ctx.IDENTIFIER().getText()
    #             modifier = attr_ctx.accessModifier().getText() if attr_ctx.accessModifier() else "public"
    #             class_def.attributes[attr_name] = (modifier, None)
    #         elif element.methodDecl():
    #             method_ctx = element.methodDecl()
    #             method_name = method_ctx.IDENTIFIER().getText()
    #             modifier = method_ctx.accessModifier().getText() if method_ctx.accessModifier() else "public"
    #             if method_ctx.ABSTRACT_KEYWORD():
    #                 if method_ctx.block():
    #                     raise Exception(f"Abstrakcyjna metoda '{method_name}' nie może mieć ciała.")
    #                 class_def.abstract_methods.add(method_name)
    #                 class_def.methods[method_name] = (modifier, None)
    #             else:
    #                 class_def.methods[method_name] = (modifier, method_ctx)
    #
    #     inherited_abstracts = set()
    #     if superclass:
    #         inherited_abstracts |= superclass.abstract_methods
    #
    #     not_implemented = inherited_abstracts - set(class_def.methods.keys())
    #     if not_implemented and not is_abstract:
    #         raise Exception(f"Klasa '{name}' nie implementuje metod abstrakcyjnych: {', '.join(not_implemented)}")
    #
    #     self.classes[name] = class_def

    def visitMainMethod(self, ctx):
        self.visit(ctx.block())

    def visitBlock(self, ctx):
        for stmt in ctx.statement():
            self.visit(stmt)

    def visitCreateStatement(self, ctx):
        var_name = ctx.IDENTIFIER(0).getText()
        class_name = ctx.IDENTIFIER(1).getText()
        class_def = self.classes.get(class_name)
        if not class_def:
            raise Exception(f"Nieznana klasa '{class_name}'")
        if class_def.is_abstract:
            raise Exception(f"Nie można tworzyć instancji klasy abstrakcyjnej '{class_name}'")

        instance = Instance(class_def)

        if ctx.argumentList():
            args = [self.visit(arg) for arg in ctx.argumentList().valueExpression()]
            self.set_constructor_attributes(instance, args)

        self.variables[var_name] = instance

    # def visitAssignment(self, ctx):
    #     target = ctx.getChild(0)
    #     value = self.visit(ctx.valueExpression())
    #
    #     if isinstance(target, OOPsyParser.IndexedAccessContext):
    #         # Przypisanie do elementu listy lub słownika, np. numbers[1] = 10
    #         collection_expr = target.getChild(0)
    #         index_expr = target.valueExpression()
    #
    #         # Obsługa nazw zmiennych lub memberAccess
    #         if isinstance(collection_expr, OOPsyParser.MemberAccessContext):
    #             collection = self.visit(collection_expr)
    #         else:
    #             var_name = collection_expr.getText()
    #             if var_name in self.variables:
    #                 collection = self.variables[var_name]
    #             else:
    #                 raise Exception(f"Nieznana zmienna lub pole: '{var_name}'")
    #
    #         index = self.visit(index_expr)
    #
    #         try:
    #             collection[index] = value
    #         except (TypeError, IndexError, KeyError):
    #             raise Exception(f"Nie można przypisać do elementu: {collection}[{index}]")
    #     elif target.getChildCount() == 1:
    #         var_name = target.getText()
    #         if var_name in self.variables:
    #             self.variables[var_name] = value
    #         else:
    #             raise Exception(f"Nieznana zmienna '{var_name}'")
    #
    #     else:
    #         obj_name = target.getChild(0).getText()
    #         attr_name = target.getChild(2).getText()
    #
    #         if obj_name == "self":
    #             if self.current_instance is None:
    #                 raise Exception("Użycie 'self' poza metodą")
    #             self.current_instance.set_attr(attr_name, value, requester=self.current_instance)
    #         else:
    #             obj = self.variables.get(obj_name)
    #             if not obj:
    #                 raise Exception(f"Nieznany obiekt '{obj_name}'")
    #             obj.set_attr(attr_name, value)
    def visitAssignment(self, ctx):
        value = self.visit(ctx.valueExpression())

        # Przypisanie do zmiennej globalnej/lokalnej
        if ctx.IDENTIFIER():
            var_name = ctx.IDENTIFIER().getText()
            if var_name in self.variables:
                self.variables[var_name] = value
            else:
                raise Exception(f"Nieznana zmienna '{var_name}'")

        # Przypisanie do pola obiektu (np. obj.x = 5)
        elif ctx.memberAccess():
            access_ctx = ctx.memberAccess()
            obj_name = access_ctx.getChild(0).getText()
            attr_name = access_ctx.getChild(2).getText()

            if obj_name == "self":
                if self.current_instance is None:
                    raise Exception("Użycie 'self' poza metodą")
                self.current_instance.set_attr(attr_name, value, requester=self.current_instance)
            else:
                obj = self.variables.get(obj_name)
                if not obj:
                    raise Exception(f"Nieznany obiekt '{obj_name}'")
                obj.set_attr(attr_name, value)

        # Przypisanie do indeksu w liście lub słowniku (np. l[2] = 7)
        elif ctx.indexedAccess():
            access_ctx = ctx.indexedAccess()

            # collection = self.visit(access_ctx.getChild(0))
            collection = self.visit(access_ctx.getChild(0))
            if collection is None:
                var_name = access_ctx.getChild(0).getText()
                collection = self.variables.get(var_name)
            index = self.visit(access_ctx.valueExpression())

            # if collection is None:
            #     raise Exception("Brak kolekcji do indeksowania")

            try:
                collection[index] = value
            except (TypeError, IndexError, KeyError):
                raise Exception(f"Nie można przypisać do elementu: {collection}[{index}]")

        else:
            raise Exception("Nieobsługiwany typ przypisania")

    def visitPrintStatement(self, ctx):
        value = self.visit(ctx.valueExpression())
        self.print_func(value)

    def visitIfStatement(self, ctx):
        condition = self.visit(ctx.logicalExpression())
        if condition:
            self.visit(ctx.block(0))
        elif ctx.ELSE_KEYWORD():
            self.visit(ctx.block(1))

    def visitLoopStatement(self, ctx):
        while True:
            self.visit(ctx.block())
            if self.visit(ctx.logicalExpression()):
                break

    def visitForStatement(self, ctx):
        var_name = ctx.IDENTIFIER().getText()
        iterable = self.visit(ctx.valueExpression())

        if not isinstance(iterable, list):
            raise Exception(f"Wyrażenie w pętli for musi być listą (otrzymano: {type(iterable).__name__})")

        for item in iterable:
            self.variables[var_name] = item
            self.visit(ctx.block())

    # def visitReturnStatement(self, ctx):
    #     raise Exception("Instrukcja 'return' obsługiwana tylko w pełnym wykonaniu funkcji (do zaimplementowania)")
    def visitReturnStatement(self, ctx):
        return

    def visitMethodCall(self, ctx):
        obj_name = ctx.IDENTIFIER(0).getText()
        method_name = ctx.IDENTIFIER(1).getText()
        obj = self.variables.get(obj_name)
        if not obj:
            raise Exception(f"Nieznany obiekt '{obj_name}'")
        method_entry = obj.class_def.methods.get(method_name)
        if not method_entry and obj.class_def.superclass:
            method_entry = obj.class_def.superclass.methods.get(method_name)
        if not method_entry:
            raise Exception(f"Obiekt '{obj_name}' nie posiada metody '{method_name}()'")

        modifier, method_ctx = method_entry
        if modifier == "private" and self.current_instance != obj:
            raise Exception(f"Metoda '{method_name}' jest prywatna i nie może być wywołana spoza klasy")

        param_names = []
        if method_ctx.paramList():
            for param in method_ctx.paramList().typedParam():
                param_names.append(param.IDENTIFIER().getText())

        arg_values = []
        if ctx.argumentList():
            arg_values = [self.visit(arg) for arg in ctx.argumentList().valueExpression()]

        if len(param_names) != len(arg_values):
            raise Exception(f"Zła liczba argumentów dla metody '{method_name}'")

        old_vars = self.variables.copy()
        for name, value in zip(param_names, arg_values):
            self.variables[name] = value

        saved_instance = self.current_instance
        self.current_instance = obj
        self.visit(method_ctx.block())
        self.current_instance = saved_instance
        self.variables = old_vars

    def visitMemberAccess(self, ctx):
        obj_name = ctx.getChild(0).getText()
        attr_name = ctx.getChild(2).getText()

        if obj_name == "self":
            if self.current_instance is None:
                raise Exception("Użycie 'self' poza metodą")
            return self.current_instance.get_attr(attr_name, requester=self.current_instance)

        obj = self.variables.get(obj_name)
        if not obj:
            raise Exception(f"Nieznany obiekt '{obj_name}'")

        if isinstance(obj, Instance):
            return obj.get_attr(attr_name)
        elif isinstance(obj, dict):
            return obj.get(attr_name)
        elif isinstance(obj, list):
            raise Exception(f"Nie można używać kropki do uzyskiwania dostępu do elementu listy '{obj_name}'")
        else:
            raise Exception(f"Obiekt '{obj_name}' nie ma atrybutów – typ: {type(obj).__name__}")

    def visitValueExpression(self, ctx):
        if ctx.INT_LITERAL():
            return int(ctx.INT_LITERAL().getText())
        if ctx.FLOAT_LITERAL():
            return float(ctx.FLOAT_LITERAL().getText())
        if ctx.STRING_LITERAL():
            return ctx.STRING_LITERAL().getText().strip('"')
        if ctx.CHAR_LITERAL():
            return ctx.CHAR_LITERAL().getText().strip("'")
        if ctx.BOOL_LITERAL_TRUE():
            return True
        if ctx.BOOL_LITERAL_FALSE():
            return False
        if ctx.IDENTIFIER():
            var_name = ctx.IDENTIFIER().getText()
            if var_name in self.variables:
                return self.variables[var_name]
            raise Exception(f"Nieznana zmienna '{var_name}'")
        if ctx.methodCall():
            return self.visit(ctx.methodCall())
        if ctx.memberAccess():
            return self.visit(ctx.memberAccess())
        # if ctx.valueExpression(0) and ctx.valueExpression(1):
        #     left = self.visit(ctx.valueExpression(0))
        #     right = self.visit(ctx.valueExpression(1))
        #     op = ctx.getChild(1).getText()
        #     return self.evaluate_binary_operation(left, op, right)
        if ctx.valueExpression(0) and ctx.valueExpression(1):
            left = self.visit(ctx.valueExpression(0))
            right = self.visit(ctx.valueExpression(1))
            op = ctx.getChild(1).getText()

            if op in ['+', '-', '*', '/', '%']:
                return self.evaluate_binary_operation(left, op, right)
            elif op in ['==', '!=', '<', '>', '<=', '>=']:
                return self.evaluate_comparison(left, op, right)
            else:
                raise Exception(f"Nieznany operator: {op}")
        if ctx.LEFT_PARENTHESIS():
            return self.visit(ctx.valueExpression(0))
        if ctx.inputCall():
            return self.visit(ctx.inputCall())
        if ctx.listLiteral():
            return self.visit(ctx.listLiteral())
        if ctx.dictLiteral():
            return self.visit(ctx.dictLiteral())
        if ctx.indexedAccess():
            return self.visit(ctx.indexedAccess())

    def visitLogicalExpression(self, ctx):
        result = self.visit(ctx.logicalTerm(0))
        for i in range(1, len(ctx.logicalTerm())):
            result = result or self.visit(ctx.logicalTerm(i))
        return result

    def visitLogicalTerm(self, ctx):
        result = self.visit(ctx.logicalFactor(0))
        for i in range(1, len(ctx.logicalFactor())):
            result = result and self.visit(ctx.logicalFactor(i))
        return result

    # def visitLogicalFactor(self, ctx):
    #     if ctx.valueExpression(1):
    #         left = self.visit(ctx.valueExpression(0))
    #         right = self.visit(ctx.valueExpression(1))
    #         op = ctx.getChild(1).getText()
    #         return self.evaluate_comparison(left, op, right)
    #     else:
    #         return self.visit(ctx.valueExpression(0))
    def visitLogicalFactor(self, ctx):
        if ctx.getChildCount() == 3 and ctx.getChild(1).getText() in ['==', '!=', '<', '>', '<=', '>=']:
            left = self.visit(ctx.getChild(0))
            right = self.visit(ctx.getChild(2))
            op = ctx.getChild(1).getText()
            return self.evaluate_comparison(left, op, right)
        elif ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        elif ctx.getChild(0).getText() == '(':
            return self.visit(ctx.logicalExpression())
        else:
            raise Exception("Nieobsługiwany logicalFactor")

    def evaluate_binary_operation(self, left, op, right):
        if op == '+':
            if isinstance(left, str) or isinstance(right, str):
                return str(left) + str(right)
            return left + right
        if op == '-':
            return left - right
        if op == '*':
            return left * right
        if op == '/':
            return left / right
        if op == '%':
            return left % right
        raise Exception(f"Nieznany operator arytmetyczny '{op}'")

    def evaluate_comparison(self, left, op, right):
        if op == '==':
            return left == right
        if op == '!=':
            return left != right
        if op == '<':
            return left < right
        if op == '>':
            return left > right
        if op == '<=':
            return left <= right
        if op == '>=':
            return left >= right
        raise Exception(f"Nieznany operator porównania '{op}'")

    def set_constructor_attributes(self, instance, args):
        def collect_attributes(class_def):
            attrs = []
            if class_def.superclass:
                attrs.extend(collect_attributes(class_def.superclass))
            attrs.extend(list(class_def.attributes.keys()))
            return attrs

        attr_names = collect_attributes(instance.class_def)
        for i, value in enumerate(args):
            if i < len(attr_names):
                instance.set_attr(attr_names[i], value)

    def visitInputCall(self, ctx):
        prompt = self.visit(ctx.valueExpression())
        return self.input_func(prompt)

    def visitCommentStatement(self, ctx):
        pass

    def visitListLiteral(self, ctx):
        elements = [self.visit(e) for e in ctx.valueExpression()]
        return elements

    def visitDictLiteral(self, ctx):
        return {
            self.visit(entry.valueExpression(0)): self.visit(entry.valueExpression(1))
            for entry in ctx.dictEntry()
        }

    # def visitLocalVarDecl(self, ctx):
    #     var_name = ctx.IDENTIFIER().getText()
    #     value = self.visit(ctx.valueExpression())
    #     # self.variables[var_name] = value
    #     type_ctx = ctx.typeName()
    #     declared_type = self.extract_type(type_ctx)
    #     actual_value = self.visit(ctx.valueExpression())
    #
    #     if not self.check_type_compatibility(declared_type, actual_value):
    #         raise Exception(
    #             f"Typ wartości ({type(actual_value).__name__}) nie pasuje do zadeklarowanego typu {declared_type}")
    #
    #     self.variables[var_name] = actual_value
    def visitLocalVarDecl(self, ctx):
        var_name = ctx.IDENTIFIER().getText()
        type_ctx = ctx.typeName()
        declared_type = self.extract_type(type_ctx)
        actual_value = self.visit(ctx.valueExpression())

        if actual_value is None:
            raise Exception(f"Nie udało się odczytać wartości zmiennej '{var_name}'")

        if not self.check_type_compatibility(declared_type, actual_value):
            raise Exception(
                f"Typ wartości ({type(actual_value).__name__}) nie pasuje do zadeklarowanego typu {declared_type}"
            )

        self.variables[var_name] = actual_value

    # def visitIndexedAccess(self, ctx):
    #     target_ctx = ctx.getChild(0)
    #     index_ctx = ctx.valueExpression()
    #
    #     index = self.visit(index_ctx)
    #
    #     # Obsługa memberAccess (np. obj.list[1])
    #     if isinstance(target_ctx, OOPsyParser.MemberAccessContext):
    #         collection = self.visit(target_ctx)
    #     else:
    #         var_name = target_ctx.getText()
    #         if var_name in self.variables:
    #             collection = self.variables[var_name]
    #         else:
    #             raise Exception(f"Nieznana zmienna lub pole: '{var_name}'")
    #
    #     try:
    #         return collection[index]
    #     except (TypeError, IndexError, KeyError):
    #         raise Exception(f"Nie można uzyskać dostępu do indeksu: {collection}[{index}]")
    def visitIndexedAccess(self, ctx):
        index = self.visit(ctx.valueExpression())

        # target = ctx.getChild(0)
        target = ctx.getChild(0)
        collection = self.visit(target)
        if collection is None:
            # Spróbuj odzyskać po nazwie, jeśli nie zadziałało
            if hasattr(target, 'getText'):
                var_name = target.getText()
                collection = self.variables.get(var_name)
            if collection is None:
                raise Exception("Brak kolekcji do indeksowania")

        # if isinstance(target, OOPsyParser.MemberAccessContext):
        #     collection = self.visit(target)
        # elif isinstance(target, OOPsyParser.IndexedAccessContext):
        #     collection = self.visit(target)
        else:
            var_name = target.getText()
            collection = self.variables.get(var_name)

        if collection is None:
            raise Exception("Brak kolekcji do indeksowania")

        try:
            return collection[index]
        except Exception as e:
            raise Exception(f"Błąd przy indeksowaniu: {collection}[{index}] — {e}")

    def extract_type(self, ctx):
        if ctx.simpleType():
            return OOPsyType(ctx.simpleType().getText())
        elif ctx.listType():
            inner = self.extract_type(ctx.listType().typeName())
            return OOPsyType("list", [inner])
        elif ctx.dictType():
            key_type = self.extract_type(ctx.dictType().typeName(0))
            value_type = self.extract_type(ctx.dictType().typeName(1))
            return OOPsyType("dict", [key_type, value_type])
        raise Exception("Nieznany typ")

    def check_type_compatibility(self, declared_type, value):
        if declared_type.base == "int" and isinstance(value, int):
            return True
        if declared_type.base == "float" and isinstance(value, float):
            return True
        if declared_type.base == "string" and isinstance(value, str):
            return True
        if declared_type.base == "char" and isinstance(value, str) and len(value) == 1:
            return True
        if declared_type.base == "bool" and isinstance(value, bool):
            return True
        if declared_type.base == "list" and isinstance(value, list):
            return all(self.check_type_compatibility(declared_type.subtypes[0], v) for v in value)
        if declared_type.base == "dict" and isinstance(value, dict):
            return all(
                self.check_type_compatibility(declared_type.subtypes[0], k) and
                self.check_type_compatibility(declared_type.subtypes[1], v)
                for k, v in value.items()
            )
        return False
