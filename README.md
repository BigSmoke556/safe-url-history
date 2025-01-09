### Descrição Detalhada do Script em Python

Este script em Python é utilizado para determinar a URL final de um link protegido, como aqueles gerados por serviços de proteção de links (por exemplo, "SafeLinks" da Microsoft). Ele segue redirecionamentos até alcançar a URL de destino final. Abaixo está a explicação detalhada de cada componente:

---

#### **Objetivo Geral**
- Rastrear e identificar a URL final de um link protegido, que frequentemente contém redirecionamentos intermediários usados para segurança, rastreamento ou gerenciamento de tráfego.

---

#### **Estrutura do Código**

1. **Importação da Biblioteca Necessária**
   ```python
   import requests
   ```
   - O módulo `requests` é uma biblioteca popular em Python para realizar solicitações HTTP.
   - Aqui, ele é utilizado para enviar uma requisição HTTP para a URL protegida e capturar informações de redirecionamento.

---

2. **Definição da URL de Entrada**
   ```python
   url = "https://na01.safelinks.protection.outlook.com/?url=http..."
   ```
   - A variável `url` contém o link protegido que será processado.
   - O link fornecido é um exemplo de uma URL protegida pelo serviço **SafeLinks** da Microsoft.

---

3. **Envio da Requisição HTTP**
   ```python
   response = requests.get(url, allow_redirects=True)
   ```
   - O método `requests.get` envia uma solicitação GET para o servidor da URL protegida.
   - O parâmetro `allow_redirects=True` instrui o Python a seguir automaticamente os redirecionamentos HTTP, capturando todas as etapas intermediárias.

---

4. **Exibição do Histórico de Redirecionamentos**
   ```python
   for i, r in enumerate(response.history, 1):
       print(f"Step {i}: {r.url} -> {r.status_code}")
   ```
   - A propriedade `response.history` retorna uma lista de objetos de resposta que representam os redirecionamentos intermediários.
   - O `enumerate` é usado para iterar sobre os redirecionamentos, numerando cada etapa.
   - Para cada etapa de redirecionamento:
     - `r.url` exibe a URL intermediária.
     - `r.status_code` exibe o código de status HTTP associado (geralmente `301` ou `302`, indicando redirecionamento).

---

5. **Exibição da URL Final**
   ```python
   print(f"Final URL: {response.url}")
   ```
   - Após seguir todos os redirecionamentos, a propriedade `response.url` contém a URL final, que é exibida no console.

---

#### **Fluxo de Execução**
1. O script começa com uma URL protegida.
2. Envia uma solicitação HTTP para a URL e segue automaticamente os redirecionamentos.
3. Lista todas as URLs intermediárias e seus códigos de status.
4. Exibe a URL final que o navegador alcançaria ao visitar o link original.

---

#### **Exemplo de Saída**
Se a URL protegida segue dois redirecionamentos, a saída do script pode ser semelhante a esta:
```
Step 1: https://na01.safelinks.protection.outlook.com/... -> 301
Step 2: http://url8672.xxxxxxxx.com.br/... -> 302
Final URL: https://www.destination.com/final-page
```

---

#### **Possíveis Aplicações**
- Rastrear URLs encurtadas ou protegidas para fins de segurança.
- Verificar se os redirecionamentos levam a destinos maliciosos.
- Automatizar o rastreamento de links em grandes volumes de dados.
- Monitorar o comportamento de URLs protegidas em sistemas de email ou plataformas web.

---

#### **Cuidados e Considerações**
- **Privacidade**: Ao rastrear URLs, dados podem ser registrados pelos servidores intermediários. Evite usar URLs que contenham informações sensíveis.
- **Limitações de Redirecionamento**: A biblioteca `requests` segue um número limitado de redirecionamentos (padrão: 30). URLs que excedam este limite podem resultar em erro.
- **Velocidade**: Rastreamento de redirecionamentos pode ser lento, especialmente se houver muitos intermediários ou conexões lentas.

---

Este script é uma ferramenta útil para desenvolvedores, analistas de segurança e outros profissionais que precisam compreender ou validar o comportamento de URLs protegidas.
