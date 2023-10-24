import random

# List of Languages names
lang = ["Python", "JavaScript", "Java", "C++", "C#", "Ruby", "Swift", "Go", "PHP", "Rust", "Kotlin", "TypeScript", "Scala", "Perl", "Haskell", "Lua", "Dart", "COBOL", "Fortran", "Ada", "Lisp", "Prolog", "Assembly", "R", "MATLAB", "Objective-C", "VHDL", "Elixir", "Clojure", "Pascal", "F#", "Groovy", "Erlang", "Julia", "LabVIEW", "Scheme", "Shell", "SQL", "Verilog", "Visual Basic", "Forth", "HTML", "SQL","C"
   
]

#selects random programming language from the given list   
random_lang = random.choice(lang)


print("Random Programming Language:", random_lang)
