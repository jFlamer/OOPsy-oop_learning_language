from grammar.OOPsyBaseVisitor import OOPsyBaseVisitor
from grammar.OOPsyParser import OOPsyParser

class SemanticChecker(OOPsyBaseVisitor):
    def __init__(self):
        super().__init__()
        self.variables = set()
        self.errors = []
        self.class_methods = {} # nazwa klasy -> {nazwa_metody: (modyfikator, param_count)}
        self.current_class = None
        self.current_superclass = None
        self.variable_types = {}

    def visitProgram(self, ctx: OOPsyParser.ProgramContext):
        # odwiedź wszystkie klasy i zapamiętaj metody
        for class_decl in ctx.classDecl():
            self.visit(class_decl)
        self.visit(ctx.mainMethod())

        if self.errors:
            raise Exception("Błędy semantyczne:\n" + "\n".join(self.errors))


    def visitClassDecl(self, ctx: OOPsyParser.ClassDeclContext):
        class_name = ctx.IDENTIFIER(0).getText()
        superclass_name = ctx.IDENTIFIER(1).getText() if ctx.INHERITS_KEYWORD() else None
        self.current_class = class_name
        self.current_superclass = superclass_name

        superclass_methods = self.class_methods.get(superclass_name, {})
        method_map = dict(superclass_methods)

        for elem in ctx.classElement():
            if elem.methodDecl():
                method_ctx = elem.methodDecl()
                method_name = method_ctx.IDENTIFIER().getText()
                is_override = bool(method_ctx.OVERRIDE_KEYWORD())
                is_final = bool(method_ctx.FINAL_KEYWORD())

                param_count = 0
                if method_ctx.paramList():
                    param_count = len(method_ctx.paramList().typedParam())

                if method_name in superclass_methods:
                    super_modifier, _ = superclass_methods[method_name]
                    if super_modifier == "final":
                        self.errors.append(
                            f"Nie można nadpisać finalnej metody '{method_name}' w klasie '{class_name}'.")

                if is_override and method_name not in superclass_methods:
                    self.errors.append(
                        f"Metoda '{method_name}' w klasie '{class_name}' ma override, ale nie istnieje w nadklasie.")

                modifier = "final" if is_final else "public"
                method_map[method_name] = (modifier, param_count)

        # 📦 Zapisz metody tej klasy
        self.class_methods[class_name] = method_map

    def visitMainMethod(self, ctx: OOPsyParser.MainMethodContext):
        self.visit(ctx.block())

        if self.errors:
            raise Exception("Błędy semantyczne:\n" + "\n".join(self.errors))

    def visitBlock(self, ctx: OOPsyParser.BlockContext):
        for stmt in ctx.statement():
            self.visit(stmt)

    def visitLocalVarDecl(self, ctx: OOPsyParser.LocalVarDeclContext):
        var_name = ctx.IDENTIFIER().getText()
        if var_name in self.variables:
            self.errors.append(f"Zmienna '{var_name}' została zadeklarowana wielokrotnie.")
        else:
            self.variables.add(var_name)
        self.visit(ctx.valueExpression())

    def visitAssignment(self, ctx: OOPsyParser.AssignmentContext):
        target = ctx.getChild(0)
        if target.getChildCount() == 1:
            var_name = target.getText()
            if var_name not in self.variables:
                self.errors.append(f"Zmienna '{var_name}' została użyta przed zadeklarowaniem.")
        self.visit(ctx.valueExpression())

    def visitValueExpression(self, ctx: OOPsyParser.ValueExpressionContext):
        if ctx.IDENTIFIER():
            var_name = ctx.IDENTIFIER().getText()
            if var_name not in self.variables:
                self.errors.append(f"Zmienna '{var_name}' została użyta przed zadeklarowaniem.")
        for child in ctx.getChildren():
            self.visit(child)
        #dzielenie przez 0
        if ctx.getChildCount() == 3:
            left = ctx.getChild(0)
            operator = ctx.getChild(1).getText()
            right = ctx.getChild(2)

            if operator in ["/", "DIV"]:
                # Sprawdzamy, czy prawa strona to 0
                if right.getText() == "0":
                    self.errors.append("Dzielenie przez 0 jest niedozwoloną operacją")


    def visitMethodCall(self, ctx: OOPsyParser.MethodCallContext):
        obj_name = ctx.IDENTIFIER(0).getText()
        method_name = ctx.IDENTIFIER(1).getText()

        if obj_name not in self.variables:
            self.errors.append(f"Obiekt '{obj_name}' nie istnieje.")
            return

        class_name = self.variable_types.get(obj_name)
        if not class_name:
            self.errors.append(f"Nieznana klasa obiektu '{obj_name}'.")
            return
        method_info = self.class_methods.get(class_name, {}).get(method_name)
        if not method_info:
            self.errors.append(f"Metoda '{method_name}' nie istnieje w klasie '{class_name}'.")
            return

        expected_args = method_info[1]
        given_args = len(ctx.argumentList().valueExpression()) if ctx.argumentList() else 0
        if expected_args != given_args:
            self.errors.append(
                f"Metoda '{method_name}' w klasie '{class_name}' oczekuje {expected_args} argumentów, podano {given_args}.")


    def visitCreateStatement(self, ctx: OOPsyParser.CreateStatementContext):
        var_name = ctx.IDENTIFIER(0).getText()
        class_name = ctx.IDENTIFIER(1).getText()

        if var_name in self.variables:
            self.errors.append(f"Zmienna '{var_name}' została zadeklarowana wielokrotnie.")
        else:
            self.variables.add(var_name)
            self.variable_types[var_name] = class_name

        if ctx.argumentList():
            for arg in ctx.argumentList().valueExpression():
                self.visit(arg)

    def visitForStatement(self, ctx: OOPsyParser.ForStatementContext):
        loop_var = ctx.IDENTIFIER().getText()

        was_already_declared = loop_var in self.variables
        self.variables.add(loop_var)

        self.visit(ctx.valueExpression())
        self.visit(ctx.block())

        if not was_already_declared:
            self.variables.remove(loop_var)


