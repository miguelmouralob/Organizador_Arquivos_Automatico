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


## 📅 Execução Automática no Windows

Este script pode ser configurado para rodar automaticamente usando o **Agendador de Tarefas do Windows**, sem precisar deixá-lo aberto o tempo todo.

---

### 🔹 Passo a passo para agendar

1. **Abrir o Agendador de Tarefas**
   - Pressione `Win + R`, digite:
     ```
     taskschd.msc
     ```
     e pressione **Enter**.

2. **Criar nova tarefa**
   - No menu da direita, clique em **Criar Tarefa** (não use "Criar Tarefa Básica").
   - Dê um nome, por exemplo: **Organizador de Arquivos**.
   - (Opcional) Marque **Executar com privilégios mais altos** para evitar problemas de permissão.

3. **Definir os gatilhos**
   - Aba **Gatilhos** → **Novo**.
   - Tipo: **Agendado**.
   - **Configuração**:
     - Repetir **Semanalmente**.
     - Marque os dias desejados (ex.: Segunda e Quinta).
     - Escolha o horário.
   - Clique em **OK**.

4. **Definir a ação**
   - Aba **Ações** → **Novo**.
   - **Programa/script**: caminho do Python, por exemplo:
     ```
     C:\Users\SeuUsuario\AppData\Local\Programs\Python\Python312\python.exe
     ```
   - **Adicionar argumentos**: caminho do script, por exemplo:
     ```
     "C:\Users\SeuUsuario\projetos\organizador.py"
     ```
   - **Iniciar em**: pasta onde o script está, por exemplo:
     ```
     C:\Users\SeuUsuario\projetos
     ```

5. **Finalizar**
   - Clique em **OK** e, se solicitado, insira sua senha de usuário do Windows.
   - O script será executado automaticamente nos dias e horários definidos.

---


## 🚀 Como usar

### 1️⃣ Clonar o repositório
```bash
git clone https://github.com/seu-usuario/organizador-arquivos.git
cd organizador-arquivos



