# JSON Parser - Un Parser JSON Construido desde Cero

## 📋 Descripción General

**json-parser** es un validador y analizador (parser) de JSON construido completamente desde cero en Python, sin dependencias externas para la lógica core. Este proyecto implementa las fases fundamentales de cualquier lenguaje o formato: **análisis léxico (tokenización)** y **análisis sintáctico (parsing)**.

Es un proyecto educativo de alta calidad que demuestra arquitectura limpia, separación de responsabilidades y princípios sólidos de diseño de software.

---

## 🎯 ¿Qué Hace Este Proyecto?

Este parser realiza dos operaciones principales:

1. **Tokenización (Lexical Analysis)**: Convierte una cadena JSON válida en una secuencia de tokens reconocibles
2. **Parsing (Syntax Analysis)**: Valida la estructura de los tokens y los traduce a estructuras de datos Python nativas

### Ejemplo de Flujo

```
JSON Input: {"name": "Alex", "age": 30}
    ↓
[Lexer] Tokeniza
    ↓
Tokens: [LEFT_BRACE, STRING("name"), COLON, STRING("Alex"), COMMA, ...]
    ↓
[Parser] Analiza sintáxis
    ↓
Resultado: {"name": "Alex", "age": 30}
```

---

## 🏗 Arquitectura del Proyecto

El proyecto sigue una arquitectura clara y modular con responsabilidades bien definidas:

### Componentes Principales

#### 1. **tokens.py** - Definición de Tokens
- Define `TokenType` con todos los tipos de tokens válidos en JSON
- Implementa la clase `Token` para representar cada unidad léxica
- Tokens soportados:
  - Estructurales: `{`, `}`, `[`, `]`
  - Separadores: `:`, `,`
  - Valores: cadenas, números, booleanos, null
  - Control: EOF (fin de archivo)

#### 2. **lexer.py** - Análisis Léxico
Responsable de leer el texto JSON y convertirlo en tokens:

- **`tokenize()`**: Método principal que escanea todo el texto
- **`read_string()`**: Extrae y valida cadenas entre comillas
- **`read_number()`**: Parsea números (enteros, decimales, notación científica)
- **`read_keyword()`**: Identifica palabras clave (`true`, `false`, `null`)

**Características:**
- Ignora automáticamente espacios en blanco (espacios, tabulaciones, saltos de línea)
- Valida cadenas no terminadas
- Soporta números en múltiples formatos (ej: `123`, `-45.67`, `1.5e10`)

#### 3. **parser.py** - Análisis Sintáctico
Implementa un parser recursivo descendente que valida la estructura JSON:

- **`parse()`**: Punto de entrada, asegura que todo el input sea consumido
- **`parse_value()`**: Identifica el tipo de valor y delega al método apropiado
- **`parse_object()`**: Analiza objetos JSON `{...}`
- **`parse_array()`**: Analiza arreglos `[...]`
- **`eat()`**: Consume un token si coincide con el tipo esperado

**Características:**
- Validación completa de sintáxis JSON
- Detección de datos superfluos después del JSON principal
- Manejo robusto de errores

#### 4. **cli.py** - Interfaz de Línea de Comandos
Proporciona un CLI profesional usando Typer:

- **`validate [file]`**: Valida JSON desde archivo o stdin
- **`version`**: Muestra la versión del programa
- Salida clara: "Valid JSON" o "Invalid JSON"
- Códigos de salida apropiados (0 para éxito, 1 para error)

---

## 📦 Requisitos

- **Python**: 3.10 o superior
- **typer**: Para la interfaz de línea de comandos
- **pytest**: Para ejecutar las pruebas (opcional, solo desarrollo)

---

## 🚀 Instalación

### 1. Clonar el Repositorio
```bash
git clone <repository-url>
cd project\ JSON\ parser
```

### 2. Crear Entorno Virtual (Recomendado)
```bash
python3.10 -m venv .venv
source .venv/bin/activate  # En Windows: .venv\Scripts\activate
```

### 3. Instalar en Modo Desarrollo
```bash
pip install -e .
```

O si deseas instalar con dependencias de desarrollo (incluyendo pytest):
```bash
pip install -e ".[dev]"
```

---

## 📖 Cómo Usar el CLI

### Comando: `validate` - Validar JSON

#### Opción 1: Validar un Archivo
```bash
json-parser validate archivo.json
```

**Ejemplo con archivo válido:**
```bash
$ echo '{"nombre": "Juan", "edad": 25}' > test.json
$ json-parser validate test.json
Valid JSON
```

**Ejemplo con archivo inválido:**
```bash
$ echo '{nombre: "Juan"}' > invalid.json
$ json-parser validate invalid.json
Invalid JSON
# Salida: código de error 1
```

#### Opción 2: Validar desde Entrada Estándar (stdin)
```bash
echo '{"status": "ok"}' | json-parser validate
```

**Ejemplos:**
```bash
# JSON válido
$ cat data.json | json-parser validate
Valid JSON

# JSON inválido
$ echo '[1, 2, 3' | json-parser validate
Invalid JSON
```

**Casos de uso prácticos:**
```bash
# Validar datos de un servidor web
curl https://api.example.com/data | json-parser validate

# Validar salida de otro programa
some-program --output-json | json-parser validate

# Validar múltiples archivos
for file in *.json; do
  echo "Validando $file..."
  json-parser validate "$file" || echo "  ❌ INVÁLIDO"
done
```

### Comando: `version` - Ver Versión
```bash
json-parser version
# Salida: json-parser v1.0
```

---

## 💡 Ejemplos de Uso Programático

Si quieres usar el parser en tu código Python:

```python
from json_parser.lexer import Lexer
from json_parser.parser import Parser

# Ejemplo 1: Validar JSON simple
json_text = '{"nombre": "Alex", "edad": 30}'

try:
    lexer = Lexer(json_text)
    tokens = lexer.tokenize()
    
    parser = Parser(tokens)
    resultado = parser.parse()
    
    print(f"JSON válido: {resultado}")
except ValueError as e:
    print(f"Error: {e}")

# Ejemplo 2: Parsear diferentes tipos JSON
ejemplos = [
    '{"punto": {"x": 10, "y": 20}}',  # Objetos anidados
    '[1, 2, 3, 4, 5]',                # Arrays
    '{"datos": [true, false, null]}', # Arrays con múltiples tipos
    '3.14159',                        # Números decimales
    '"Solo una cadena"'               # Cadena simple
]

for json_str in ejemplos:
    try:
        lexer = Lexer(json_str)
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        print(f"✓ {json_str} → {parser.parse()}")
    except ValueError as e:
        print(f"✗ {json_str} → Error: {e}")
```

---

## 🧪 Ejecutar las Pruebas

El proyecto incluye suite de pruebas exhaustiva con **pytest**:

```bash
# Ejecutar todas las pruebas
pytest

# Ejecutar con salida detallada
pytest -v

# Ejecutar solo tests del lexer
pytest test/test_lexer.py

# Ejecutar solo tests del parser
pytest test/test_parser.py

# Ver cobertura de tests
pytest --cov=src/json_parser
```

### Suite de Pruebas

#### `test_lexer.py` - Tokenización
- ✓ Tokens de estructuras básicas `{}`, `[]`
- ✓ Ignorar espacios en blanco
- ✓ Tokens de cadenas con valores
- ✓ Objetos con múltiples campos
- ✓ Detección de cadenas no terminadas

#### `test_parser.py` - Parsing
- ✓ Parsing de números
- ✓ Parsing de objetos simples
- ✓ Parsing de arreglos
- ✓ Detección de datos superfluos después del JSON

#### `test_tokens.py` - Tokens
- ✓ Creación correcta de tokens
- ✓ Conservación de tipo y valor

---

## 📁 Estructura del Proyecto

```
project JSON parser/
├── pyproject.toml              # Configuración del proyecto
├── README.md                   # Este archivo
├── src/
│   └── json_parser/           # Paquete principal
│       ├── __init__.py        # Inicializador del paquete
│       ├── cli.py             # Interfaz de línea de comandos
│       ├── lexer.py           # Análisis léxico (tokenización)
│       ├── parser.py          # Análisis sintáctico (parsing)
│       └── tokens.py          # Definición de tokens
├── test/                       # Suite de pruebas
│   ├── test_lexer.py          # Tests del lexer
│   ├── test_parser.py         # Tests del parser
│   └── test_tokens.py         # Tests de tokens
└── .venv/                     # Entorno virtual (creado localmente)
```

---

## 🔍 Flujo de Ejecución Detallado

### Durante la Validación

```
1. CLI recibe input (archivo o stdin)
2. Lexer.tokenize() 
   └─ Escanea cada carácter
   └─ Agrupa en tokens semánticos
   └─ Ignora espacios en blanco
3. Parser.parse()
   └─ Consume tokens según reglas JSON
   └─ Construye estructura de datos
   └─ Valida sintáxis completa
4. Si todo es válido → "Valid JSON"
5. Si hay error → Excepción capturada y "Invalid JSON"
```

### Ejemplo con Trazado Completo

```
Input: {"x": 123}

LEXER OUTPUT:
Token(LEFT_BRACE, None)
Token(STRING, "x")
Token(COLON, None)
Token(NUMBER, 123)
Token(RIGHT_BRACE, None)
Token(EOF, None)

PARSER EXECUTION:
parse() → parse_value() → parse_object()
├─ eat(LEFT_BRACE)
├─ Llave "x" encontrada
├─ eat(COLON)
├─ parse_value() → número 123
├─ eat(RIGHT_BRACE)
└─ Retorna: {"x": 123}

SALIDA FINAL: Valid JSON ✓
```

---

## 🎓 Conceptos Educativos

Este proyecto es excelente para aprender:

1. **Análisis Léxico**: Cómo los lenguajes/parsers identifican tokens
2. **Análisis Sintáctico**: Cómo validan la estructura usando recursión
3. **Máquinas de Estado**: El lexer implementa un autómata finito
4. **Parser Recursivo Descendente**: Patrón usado en muchos compiladores
5. **Manejo de Excepciones**: Errores semánticos vs. sintácticos
6. **Arquitectura de Software**: Separación clara de responsabilidades
7. **Testing**: Suite de pruebas para componentes críticos

---

## ⚠️ Limitaciones Conocidas

Aunque el parser es completamente funcional, algunas limitaciones educativas:

- No genera números de línea/columna en errores (solo tipo de error)
- No soporta escape sequences complejos en strings
- No valida restricciones de profundidad (podría causar stack overflow en JSON muy profundo)

Estas limitaciones son intencionales para mantener el código educativo y legible.

---

## 🤝 Notas Técnicas

### Por Qué Este Diseño

1. **Sin dependencias core**: El parser/lexer no depende de librerías, solo de Python puro
2. **Typer para CLI**: Minimiza boilerplate, proporciona ayuda automática y validación
3. **Pruebas completas**: `pytest` es estándar en Python para testing
4. **Estructura modular**: Cada componente tiene una razón de ser y puede testearse independientemente

### Mejoras Futuras Potenciales

- [ ] Agregar información de línea/columna en errores
- [ ] Soporte para escape sequences JSON completo
- [ ] Modo de "pretty-print" para formatear JSON
- [ ] Soporte para comentarios (variante JSONC)
- [ ] Performance profiling para archivos grandes
- [ ] Streaming parser para archivos muy grandes

---

## 📞 Soporte y Contribuciones

Para reportar bugs o sugerir mejoras, usa el sistema de issues del repositorio.

---

**Última actualización**: Marzo 2026  
**Versión**: 1.0  
**Estado**: Producción (Validación funcional completa)
