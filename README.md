# Organizador Automático de Arquivos

Script em Python que organiza automaticamente arquivos de uma pasta em **subpastas** de acordo com a extensão.  
Exemplo:  
- `.pdf`, `.docx` → `Documentos`  
- `.jpg`, `.png` → `Imagens`  
- `.mp3` → `Musicas`  
- `.mp4` → `Videos`  

Também registra um **log** (`organizador_log.txt`) com cada movimentação feita.

---

## 📂 Funcionalidades

- Organiza arquivos por extensão usando um **dicionário de mapeamento**.
- Cria automaticamente as pastas de destino, se não existirem.
- Garante nomes únicos (evita sobrescrever arquivos existentes).
- Possui modo **dry-run** (simulação, sem mover de fato).
- Registra todas as ações em um arquivo de log com data e hora.
- Pode mover extensões desconhecidas para a pasta `Outros`.

---

## 🚀 Como usar

### 1️⃣ Clonar o repositório
```bash
git clone https://github.com/seu-usuario/organizador-arquivos.git
cd organizador-arquivos
