# note

## date : 2022/02/15

- start vscode using powershell using proxy : `code --proxy-server="socks5://127.0.0.1:1080"`
- install vim extension through **vsix**
- enable easymotion plugin through setting `"vim.easymotion": true,`
- other setting for vim

## date : 2022/06/06
- string.format()
- replace_field format:
    - replacement_field ::=  "{" [field_name] ["!" conversion] [":" format_spec] "}"
    - field_name        ::=  arg_name ("." attribute_name | "[" element_index "]")*
    - arg_name          ::=  [identifier | digit+]
    - attribute_name    ::=  identifier
    - element_index     ::=  digit+ | index_string
    - index_string      ::=  <any source character except "]"> +
    - conversion        ::=  "r" | "s" | "a"
    - format_spec       ::=  <described in the next section>
