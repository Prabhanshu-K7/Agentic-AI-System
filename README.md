# 🐍 Python Interactive Computing Environment  

A **robust environment** for interactive programming in Python, featuring **IPython**, **Jupyter integration**, and support for **modern computational workflows**.  
Ideal for **data science**, **research**, and **rapid prototyping**.  

---

## 📑 Table of Contents  
- [Overview](#-overview)  
- [Features](#-features)  
- [Installation](#-installation)  
- [Usage](#-usage)  
- [Configuration](#-configuration)  
- [Project Structure](#-project-structure)  
- [Contributing](#-contributing)  
- [License](#-license)  
- [Acknowledgments](#-acknowledgments)  

---

## 🔎 Overview  
This repository provides **tools and configuration** for interactive Python development using **IPython** and **Jupyter**. It supports:  
- Robust code execution  
- Dynamic introspection  
- Enhanced shell access  
- Rich extension capabilities  

It is particularly well-suited for:  
- 📊 Data Science workflows  
- 🔬 Research projects  
- 🧪 Prototyping and experimentation  

---

## 🚀 Features  
- 🖥️ **Interactive Python shell** with:  
  - Automatic history  
  - Object introspection  
  - Command completion  
  - System shell integration  

- 📒 **Jupyter Notebook support** for rich, browser-based computation.  

- ⚙️ **Custom configuration** via profiles and extension loading (`ipython.1`, `extensionRequires.js`).  

- 🔗 **Kernel support** for Python 3, using `ipykernel_launcher` (`kernel.json`).  

---

## ⚡ Installation  

### Requirements  
- Python 3.x  
- pip  

### Steps  
```bash
git clone https://github.com/Prabhanshu-K7/Agentic-AI-System.git
cd Agentic-AI-System
pip install -r requirements.txt
```

---

## 🛠️ Usage  

### Start an interactive IPython session:  
```bash
ipython
```

### Launch Jupyter Notebook:  
```bash
jupyter notebook
```

### Customize Your Environment  
- Modify configuration files generated in the `IPYTHONDIR` (default: `$HOME/.ipython`).  
- Generate default configs:  
  ```bash
  ipython profile create
  ```
- Explore advanced options:  
  ```bash
  ipython --help
  ```

---

## ⚙️ Configuration  
- All configuration files are stored in the directory defined by the `IPYTHONDIR` environment variable.  
- To generate default configuration files:  
  ```bash
  ipython profile create
  ```
- For Jupyter extension integration, additional JavaScript and configs are available in this repo (`extensionRequires.js`).  

---

## 📂 Project Structure  

| File/Folder            | Description                                    |
|-------------------------|------------------------------------------------|
| `ipython.1`            | Manpage for IPython CLI usage                  |
| `kernel.json`          | Configuration for Python Jupyter kernel        |
| `extensionRequires.js` | JavaScript required for Jupyter/IPython extensions |

---

## 🤝 Contributing  
Contributions are **welcome!** 🎉  

1. Fork this repository  
2. Create a new branch (`feature/your-feature-name`)  
3. Commit your changes  
4. Push to your fork  
5. Open a Pull Request  

👉 If you’re planning significant changes, please open an issue first to discuss your ideas.  

---

## 📜 License  
This project is licensed under the **MIT License**.  
See the [LICENSE](./LICENSE) file for details.  

---

## 🙏 Acknowledgments  
Special thanks to:  
- **IPython Development Team**  
- **Project Jupyter**  
- **Python Community Contributors**  

💬 For questions or support, please raise an [Issue](../../issues).  

---
