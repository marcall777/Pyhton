from flask import Flask

app = Flask(__name__) 

@app.route('/curriculo')  
def curriculo():
    return """
    <html>
        <head>
            <title>Currículo</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    line-height: 1.6;
                    margin: 20px;
                    background-color: #f4f4f9;
                    color: #333;
                }
                h1, h2 {
                    color: #4CAF50;
                }
                h1 {
                    border-bottom: 2px solid #4CAF50;
                    padding-bottom: 5px;
                }
                ul {
                    margin: 10px 0;
                    padding-left: 20px;
                }
                ul li {
                    margin: 5px 0;
                }
            </style>
        </head>
        <body>
            <h1>Currículo</h1>
            <h2>Dados Pessoais</h2>
            <p><strong>Nome:</strong> João da Silva</p>
            <p><strong>Email:</strong> joao.silva@email.com</p>
            <p><strong>Telefone:</strong> (11) 98765-4321</p>
            
            <h2>Formação Acadêmica</h2>
            <ul>
                <li>Bacharelado em Ciência da Computação - Universidade XYZ (2015 - 2019)</li>
                <li>Curso Técnico em Informática - Escola Técnica ABC (2012 - 2014)</li>
            </ul>
            
            <h2>Experiência Profissional</h2>
            <ul>
                <li>Desenvolvedor Full Stack - Empresa 123 (2020 - Presente)</li>
                <li>Estagiário em Desenvolvimento Web - Empresa XYZ (2018 - 2019)</li>
            </ul>
            
            <h2>Habilidades</h2>
            <ul>
                <li>Python, Flask, Django</li>
                <li>HTML, CSS, JavaScript</li>
                <li>Banco de Dados: MySQL, PostgreSQL</li>
                <li>Controle de Versão: Git</li>
            </ul>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)