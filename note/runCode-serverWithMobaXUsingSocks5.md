# Code-server
````
https://github.com/cdr/code-server/tree/v3.9.0
````


# MobaXterm command for code-server
````
# -o "ProxyCommand=nc -X 5 -x 127.0.0.1:1080 %h %p"
# is using socks5 as proxy
ssh -N -L 8080:127.0.0.1:8080 root@107.X.79.246 -o "ProxyCommand=nc -X 5 -x 127.0.0.1:1080 %h %p"
````

# using web broswer to connect to vscode 
http://127.0.0.1:8080



## url reference
- https://superuser.com/questions/454210/how-can-i-use-ssh-with-a-socks-5-proxy
- https://stackoverflow.com/questions/19161960/connect-with-ssh-through-a-proxy
- [using vscode in web browser](https://www.windowscentral.com/how-use-visual-studio-code-web-browser)
