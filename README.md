# safe-url-history
Este script rastreia redirecionamentos em links protegidos, exibindo cada etapa até alcançar a URL final. Utiliza requests para enviar uma requisição GET com allow_redirects=True, listando redirecionamentos (response.history) e a URL final (response.url). Útil para verificar destinos seguros.
