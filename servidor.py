from decimal import Decimal, InvalidOperation
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import json

from carrinho import Carrinho, FretePadrao, FreteExpresso


def cotacao(dados):
    modos = {"padrao": FretePadrao, "expresso": FreteExpresso}
    carrinho = Carrinho(modos[dados["modalidade"]]())
    itens = dados["itens"]
    if not isinstance(itens, list):
        raise ValueError("Informe uma lista de itens.")
    for item in itens:
        carrinho.adicionar(item["nome"], Decimal(str(item["preco"])), item["quantidade"])
    subtotal, frete, total = carrinho.cotar()
    return dict(subtotal=str(subtotal), frete=str(frete), total=str(total))


class Aplicacao(BaseHTTPRequestHandler):
    def responder(self, status, tipo, corpo):
        self.send_response(status)
        self.send_header("Content-Type", tipo)
        self.send_header("Content-Length", str(len(corpo)))
        self.end_headers()
        self.wfile.write(corpo)

    def do_GET(self):
        if self.path != "/":
            return self.send_error(404)
        pagina = Path(__file__).with_name("index.html").read_bytes()
        self.responder(200, "text/html; charset=utf-8", pagina)

    def do_POST(self):
        if self.path != "/cotacao":
            return self.send_error(404)
        try:
            tamanho = int(self.headers.get("Content-Length", 0))
            if not 0 < tamanho <= 32000:
                raise ValueError("Tamanho da solicitação inválido.")
            resultado = cotacao(json.loads(self.rfile.read(tamanho)))
            status = 200
        except (ValueError, InvalidOperation, KeyError, TypeError, AttributeError) as erro:
            status = 400
            resultado = {"erro": str(erro) if isinstance(erro, ValueError) else "Revise os dados dos itens."}
        self.responder(status, "application/json", json.dumps(resultado).encode())


if __name__ == "__main__":
    print("Abra http://127.0.0.1:8000 no navegador.", flush=True)
    ThreadingHTTPServer(("127.0.0.1", 8000), Aplicacao).serve_forever()
