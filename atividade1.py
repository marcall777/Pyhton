from flask import Flask

app = Flask(__name__)

@app.route('/decorator') 
def hello():
    return """<html>
        <head>
            <title>Conceito de Decorator</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    line-height: 1.6;
                    margin: 20px;
                    background-color: #f4f4f9;
                    color: #333;
                }
                h1 {
                    color: #4CAF50;
                }
                h2 {
                    color: #2E8B57;
                }
                p {
                    margin: 10px 0;
                }
                ul {
                    margin: 10px 0;
                    padding-left: 20px;
                }
                ul li {
                    margin: 5px 0;
                }
                pre {
                    background: #eee;
                    padding: 10px;
                    border-left: 4px solid #4CAF50;
                    overflow-x: auto;
                }
                code {
                    font-family: "Courier New", Courier, monospace;
                    background: #f9f9f9;
                    padding: 2px 4px;
                    border-radius: 4px;
                }
            </style>
        </head>
        <body>
            <h1>O que é um Decorator em Python?</h1>
            <p>Um <strong>decorator</strong> em Python é uma função que modifica o comportamento de outra função ou método. Ele é utilizado para adicionar funcionalidades a funções existentes de maneira elegante e reutilizável.</p>
            
            <h2>Para que ele serve?</h2>
            <p>Decorators são usados para:</p>
            <ul>
                <li>Adicionar funcionalidades a funções ou métodos sem alterar seu código original.</li>
                <li>Facilitar a reutilização de código.</li>
                <li>Manter o código mais limpo e organizado.</li>
            </ul>
            
            <h2>Como ele é utilizado no Flask?</h2>
            <p>No Flask, decorators são usados para definir rotas. Por exemplo:</p>
            <pre>
@app.route('/decorator')
def hello():
    return "Exemplo de rota com decorator"
            </pre>
            <p>O <code>@app.route</code> é um decorator que associa uma URL específica a uma função Python.</p>
        </body>
    </html>"""



if __name__ == '__main__':
    app.run(debug=True) 