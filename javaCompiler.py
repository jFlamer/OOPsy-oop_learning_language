from grammar.OOPsyBaseVisitor import OOPsyBaseVisitor
from grammar.OOPsyParser import OOPsyParser

TYPE_MAP = {
        "int": "int",
        "float": "float",
        "bool": "boolean",
        "char": "char",
        "string": "String",
        "list": "ArrayList",
        "dict": "HashMap"
    }

class JavaCompiler(OOPsyBaseVisitor):
    def __init__(self):
        self.output = []
        self.current_class = None
        self.classes_with_parents = {}
        self.class_param_counts = {}
        self.superclass_param_map = {}
        self.class_fields = {}
        self.variable_types = {}
        self.imports = set()

    # def compile(self, tree):
    #     self.visit(tree)
    #     return "\n".join(self.output)
    def compile(self, tree):
        self.visit(tree)
        return "\n".join(sorted(self.imports) + [""] + self.output)

    def visitProgram(self, ctx):
        for class_decl in ctx.classDecl():
            self.visit(class_decl)
        self.visit(ctx.mainMethod())

    def visitClassDecl(self, ctx):
        class_name = ctx.IDENTIFIER(0).getText()
        self.current_class = class_name
        is_abstract = ctx.ABSTRACT_KEYWORD() is not None
        prefix = "abstract " if is_abstract else ""
        if ctx.INHERITS_KEYWORD():
            base_class = ctx.IDENTIFIER(1).getText()
            self.superclass_param_map[class_name] = base_class
        extends_clause = f" extends {ctx.IDENTIFIER(1).getText()}" if ctx.INHERITS_KEYWORD() else ""
        self.output.append(f"{prefix}class {class_name}{extends_clause} {{")
        for element in ctx.classElement():
            self.visit(element)
        self.output.append("}")

    def visitAttributeDecl(self, ctx):
        name = ctx.IDENTIFIER().getText()
        modifier = ctx.accessModifier().getText() if ctx.accessModifier() else "public"
        type_ = TYPE_MAP.get(ctx.typeName().getText(), ctx.typeName().getText())

        if self.current_class not in self.class_fields:
            self.class_fields[self.current_class] = {}
        self.class_fields[self.current_class][name] = type_

        self.output.append(f"    {modifier} {type_} {name};")

    # def visitMethodDecl(self, ctx):
    #     name = ctx.IDENTIFIER().getText()
    #     modifier = ctx.accessModifier().getText() if ctx.accessModifier() else "public"
    #     params = self.visit(ctx.paramList()) if ctx.paramList() else ""
    #     self.output.append(f"    {modifier} void {name}({params}) {{")
    #     self.visit(ctx.block())
    #     self.output.append("    }")

    def visitMethodDecl(self, ctx):
        name = ctx.IDENTIFIER().getText()
        access = ctx.accessModifier().getText() if ctx.accessModifier() else "public"
        is_abstract = ctx.ABSTRACT_KEYWORD() is not None
        is_final = ctx.FINAL_KEYWORD() is not None
        is_override = ctx.OVERRIDE_KEYWORD() is not None
        if is_abstract and is_final:
            raise Exception(f"Nie można łączyć 'abstract' i 'final' w metodzie '{name}'")

        params = self.visit(ctx.paramList()) if ctx.paramList() else ""
        modifiers = [access]
        if is_abstract:
            modifiers.insert(0, "abstract")
        if is_final:
            modifiers.insert(0, "final")

        # Generujemy metodę
        if is_abstract:
            self.output.append(f"    {' '.join(modifiers)} void {name}({params});")
        else:
            self.output.append(f"    {' '.join(modifiers)} void {name}({params}) {{")
            self.visit(ctx.block())
            self.output.append("    }")

    def visitConstructorDecl(self, ctx):
        params = []
        assignments = []
        param_names = []

        if ctx.paramList():
            for param in ctx.paramList().typedParam():
                type_text = TYPE_MAP.get(param.typeName().getText(), param.typeName().getText())
                name_text = param.IDENTIFIER().getText()
                params.append(f"{type_text} {name_text}")
                param_names.append(name_text)
                assignments.append(f"        this.{name_text} = {name_text};")

        self.class_param_counts[self.current_class] = param_names

        self.output.append(f"    public {self.current_class}({', '.join(params)}) {{")

        if self.current_class in self.superclass_param_map:
            base_class_name = self.superclass_param_map[self.current_class]
            base_param_names = self.class_param_counts.get(base_class_name, [])
            super_args = param_names[:len(base_param_names)]
            self.output.append(f"        super({', '.join(super_args)});")

            assignments = [
                f"        this.{name} = {name};"
                for name in param_names[len(base_param_names):]
            ]

        self.output.extend(assignments)
        self.output.append("    }")

    def visitParamList(self, ctx):
        params = []
        for param in ctx.typedParam():
            name = param.IDENTIFIER().getText()
            type_ = TYPE_MAP.get(param.typeName().getText(), param.typeName().getText())
            params.append(f"{type_} {name}")
        return ", ".join(params)

    def visitArgumentList(self, ctx):
        return ", ".join(self.visit(expr) for expr in ctx.valueExpression())

    def visitMainMethod(self, ctx):
        self.output.append("public class Main {")
        self.output.append("    public static void main(String[] args) {")
        self.visit(ctx.block())
        self.output.append("    }")
        self.output.append("}")

    def visitBlock(self, ctx):
        for stmt in ctx.statement():
            self.visit(stmt)

    def visitCreateStatement(self, ctx):
        var = ctx.IDENTIFIER(0).getText()
        typ = ctx.IDENTIFIER(1).getText()
        self.variable_types[var] = typ
        args = ""
        if ctx.argumentList():
            args = self.visit(ctx.argumentList())
        self.output.append(f"        {typ} {var} = new {typ}({args});")

    def visitAssignment(self, ctx):
        target = ctx.getChild(0)
        value_expr = ctx.valueExpression()
        value = self.visit(value_expr)

        # if isinstance(target, OOPsyParser.IndexedAccessContext):
        #     target_code = self.visit(target.getChild(0))  # nazwa listy/słownika
        #     index_code = self.visit(target.valueExpression())
        #     self.output.append(f"        {target_code}.set({index_code}, {value});")
        #     return
        if ctx.indexedAccess():
            ia = ctx.indexedAccess()
            if ia.IDENTIFIER():
                target = ia.IDENTIFIER().getText()
            elif ia.memberAccess():
                target = self.visit(ia.memberAccess())
            else:
                target = "UNKNOWN"

            index = self.visit(ia.valueExpression())
            self.output.append(f"        {target}.set({index}, {value});")
            return

        if target.getChildCount() > 1:
            target_code = self.visitMemberAccess(target)
            var_name = target.getChild(0).getText()
            attr_name = target.getChild(2).getText()
        else:
            target_code = target.getText()
            var_name = None
            attr_name = None

        if value_expr.inputCall():
            prompt = self.visit(value_expr.inputCall().valueExpression())
            self.ensure_scanner_initialized()
            self.output.append(f"        System.out.print({prompt});")

            # domyślny typ to string
            field_type = "String"

            if var_name and attr_name:
                class_name = self.variable_types.get(var_name)
                if class_name and class_name in self.class_fields:
                    field_type = self.class_fields[class_name].get(attr_name, "String")

            if field_type == "int":
                self.output.append(f"        {target_code} = Integer.parseInt(scanner.nextLine());")
            elif field_type == "float":
                self.output.append(f"        {target_code} = Float.parseFloat(scanner.nextLine());")
            elif field_type == "boolean":
                self.output.append(f"        {target_code} = Boolean.parseBoolean(scanner.nextLine());")
            else:
                self.output.append(f"        {target_code} = scanner.nextLine();")
        else:
            value = self.visit(value_expr)
            self.output.append(f"        {target_code} = {value};")

    def visitPrintStatement(self, ctx):
        value = self.visit(ctx.valueExpression())
        self.output.append(f"        System.out.println({value});")

    def visitValueExpression(self, ctx):
        if ctx.methodCall():
            return self.visit(ctx.methodCall())
        if ctx.memberAccess():
            return self.visit(ctx.memberAccess())
        if ctx.IDENTIFIER():
            return ctx.IDENTIFIER().getText()
        if ctx.INT_LITERAL():
            return ctx.INT_LITERAL().getText()
        if ctx.STRING_LITERAL():
            return ctx.STRING_LITERAL().getText()
        if ctx.BOOL_LITERAL_TRUE():
            return "true"
        if ctx.BOOL_LITERAL_FALSE():
            return "false"
        if ctx.valueExpression(0) and ctx.valueExpression(1):
            left = self.visit(ctx.valueExpression(0))
            right = self.visit(ctx.valueExpression(1))
            op = ctx.getChild(1).getText()
            return f"({left} {op} {right})"
        if ctx.LEFT_PARENTHESIS():
            return f"({self.visit(ctx.valueExpression(0))})"
        if ctx.inputCall():
            prompt = self.visit(ctx.inputCall().valueExpression())
            self.ensure_scanner_initialized()
            tmp_var = f"__input_tmp_{len(self.output)}"
            self.output.append(f'        System.out.print({prompt});')
            self.output.append(f'        String {tmp_var} = scanner.nextLine();')
            return tmp_var
        if ctx.listLiteral():
            return self.visit(ctx.listLiteral())
        if ctx.dictLiteral():
            return self.visit(ctx.dictLiteral())
        if ctx.indexedAccess():
            return self.visit(ctx.indexedAccess())
        return ""

    def visitMemberAccess(self, ctx):
        base = ctx.getChild(0).getText()
        field = ctx.getChild(2).getText()
        if base == "self":
            return f"this.{field}"
        return f"{base}.{field}"

    def visitIfStatement(self, ctx):
        condition = self.visit(ctx.logicalExpression())
        self.output.append(f"        if ({condition}) {{")
        self.visit(ctx.block(0))
        self.output.append("        }")
        if ctx.ELSE_KEYWORD():
            self.output.append("        else {")
            self.visit(ctx.block(1))
            self.output.append("        }")

    def visitLoopStatement(self, ctx):
        self.output.append("        do {")
        self.visit(ctx.block())
        condition = self.visit(ctx.logicalExpression())
        self.output.append(f"        }} while (!({condition}));")

    def visitForStatement(self, ctx):
        loop_var = ctx.IDENTIFIER().getText()
        iterable_expr = self.visit(ctx.valueExpression())

        tmp_iterable = f"__list_{len(self.output)}"
        self.output.append(f"        for (Object {loop_var} : {iterable_expr}) {{")
        self.visit(ctx.block())
        self.output.append("        }")

    def visitLocalVarDecl(self, ctx):
        var_name = ctx.IDENTIFIER().getText()
        expr = self.visit(ctx.valueExpression())
        self.output.append(f"        var {var_name} = {expr};")

    # def visitListLiteral(self, ctx):
    #     elements = [self.visit(e) for e in ctx.valueExpression()]
    #     return f"java.util.Arrays.asList({', '.join(elements)})"
    def visitListLiteral(self, ctx):
        elements = [self.visit(e) for e in ctx.valueExpression()]
        return f"new java.util.ArrayList<>(java.util.Arrays.asList({', '.join(elements)}))"

    # def visitDictLiteral(self, ctx):
    #     entries = []
    #     for entry in ctx.dictEntry():
    #         key = self.visit(entry.valueExpression(0))
    #         value = self.visit(entry.valueExpression(1))
    #         entries.append(f"put({key}, {value})")
    #
    #     tmp_var = f"__map_{len(self.output)}"
    #     self.output.append(f"        java.util.HashMap<Object, Object> {tmp_var} = new java.util.HashMap<>();")
    #     for entry in ctx.dictEntry():
    #         key = self.visit(entry.valueExpression(0))
    #         value = self.visit(entry.valueExpression(1))
    #         self.output.append(f"        {tmp_var}.put({key}, {value});")
    #     return tmp_var
    def visitDictLiteral(self, ctx):
        tmp_var = f"__map_{len(self.output)}"
        self.output.append(f"        java.util.HashMap<Object, Object> {tmp_var} = new java.util.HashMap<>();")
        for entry in ctx.dictEntry():
            key = self.visit(entry.valueExpression(0))
            value = self.visit(entry.valueExpression(1))
            self.output.append(f"        {tmp_var}.put({key}, {value});")
        return tmp_var

    def visitLogicalExpression(self, ctx):
        if len(ctx.logicalTerm()) > 1:
            left = self.visit(ctx.logicalTerm(0))
            right = self.visit(ctx.logicalTerm(1))
            return f"{left} || {right}"
        return self.visit(ctx.logicalTerm(0))

    def visitLogicalTerm(self, ctx):
        if len(ctx.logicalFactor()) > 1:
            left = self.visit(ctx.logicalFactor(0))
            right = self.visit(ctx.logicalFactor(1))
            return f"{left} && {right}"
        return self.visit(ctx.logicalFactor(0))

    def visitLogicalFactor(self, ctx):
        if ctx.getChildCount() == 3 and ctx.getChild(1).getText() in ['==', '!=', '<', '>', '<=', '>=']:
            left = self.visit(ctx.valueExpression(0))
            op = ctx.getChild(1).getText()
            right = self.visit(ctx.valueExpression(1))
            return f"{left} {op} {right}"
        elif ctx.logicalExpression():
            return f"({self.visit(ctx.logicalExpression())})"
        else:
            return self.visit(ctx.valueExpression(0))

    def visitExpressionStatement(self, ctx):
        expr = self.visit(ctx.anyExpression())
        if expr:
            self.output.append(f"        {expr};")

    def visitAnyExpression(self, ctx):
        if ctx.valueExpression():
            return self.visit(ctx.valueExpression())
        if ctx.PRINT_KEYWORD():
            value = self.visit(ctx.valueExpression(0))
            return f"System.out.println({value})"

    def visitMethodCall(self, ctx):
        obj = ctx.IDENTIFIER(0).getText()
        method = ctx.IDENTIFIER(1).getText()
        args = self.visit(ctx.argumentList()) if ctx.argumentList() else ""
        return f"{obj}.{method}({args})"

    def visitArgumentList(self, ctx):
        return ", ".join(self.visit(expr) for expr in ctx.valueExpression())

    def visitReturnStatement(self, ctx):
        if ctx.valueExpression():
            value = self.visit(ctx.valueExpression())
            self.output.append(f"        return {value};")
        else:
            self.output.append("        return;")

    def visitBreakStatement(self, ctx):
        self.output.append("        break;")

    def visitContinueStatement(self, ctx):
        self.output.append("        continue;")

    def visitSuperCallStatement(self, ctx):
        args = self.visit(ctx.argumentList()) if ctx.argumentList() else ""
        self.output.append(f"        super({args});")

    def visitCommentStatement(self, ctx):
        comment = ctx.LINE_COMMENT().getText()
        self.output.append(f"        {comment}")

    def visitIndexedAccess(self, ctx):
        if ctx.IDENTIFIER():
            target = ctx.IDENTIFIER().getText()
        elif ctx.memberAccess():
            target = self.visit(ctx.memberAccess())
        else:
            target = "UNKNOWN"

        index = self.visit(ctx.valueExpression())
        return f"{target}.get({index})"

    def ensure_scanner_initialized(self):
        # self.imports.add("import java.util.Scanner;")
        if "import java.util.Scanner;" not in self.output:
            self.output.insert(0, "import java.util.Scanner;")
        if not any("Scanner scanner = new Scanner(System.in);" in line for line in self.output):
            for i, line in enumerate(self.output):
                if "public static void main" in line:
                    self.output.insert(i + 1, "        Scanner scanner = new Scanner(System.in);")
                    break

    def add_imports_for(self, type_name):
        if type_name == "ArrayList":
            self.imports.add("import java.util.ArrayList;")
            self.imports.add("import java.util.Arrays;")
        elif type_name == "HashMap":
            self.imports.add("import java.util.HashMap;")


