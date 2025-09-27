# 🛁 Sistema de Gestão de Atendimento de Lava-Rápido (CLI) em Python(Pt-br)

Este é um projeto de linha de comando que simula o registro de serviços em um lava-rápido, calculando automaticamente a hora prevista de entrega do veículo com base no tipo de serviço escolhido.

Este projeto é uma excelente prática para:

* **Manipulação de Data e Hora:** Uso das classes `datetime` e `timedelta` para cálculos de tempo.
* **Modularização:** Organização do código com funções (`def`) separadas para cada tipo de serviço.
* **Formatação de Saída:** Uso de `f-strings` para apresentar um "Extrato de Serviço" formatado e legível.
* **Estrutura de Menu:** Controle de fluxo com um loop `while` para manter a aplicação interativa.

---

## 🚀 Funcionalidades

O sistema opera através de um menu interativo, permitindo registrar o serviço com base no tamanho do veículo e gerar um extrato detalhado.

| Opção | Tipo de Veículo | Duração Prevista |
| :---: | :---: | :---: |
| **1** | Carro Pequeno | 30 minutos |
| **2** | Carro Médio | 45 minutos |
| **3** | Carro Grande | 60 minutos |
| **4** | Carro de Luxo | 90 minutos |
| **5** | Sair | - |

Para cada serviço, o programa gera um **Extrato de Serviço** contendo:

* O tipo de veículo.
* A hora e data do **Início do Serviço**.
* A hora e data da **Entrega Prevista** (calculada automaticamente).
* O valor cobrado pelo serviço.

---

## 🛁 Python Car Wash Service Management System (CLI)(En)

This is a command-line project that simulates service registration at a car wash, automatically calculating the estimated delivery time based on the type of service selected.

This project is excellent practice for:

* **Date and Time Manipulation:** Use of the `datetime` and `timedelta` classes for time calculations.
* **Modularization:** Organizing code with separate functions (`def`) for each service type.
* **Output Formatting:** Use of `f-strings` to present a formatted and legible "Service Receipt."
* **Menu Structure:** Flow control with a `while` loop to keep the application interactive.

## 🚀 Features

The system operates through an interactive menu, allowing service registration based on vehicle size and generating a detailed receipt.

| Option | Vehicle Type | Estimated Duration |
| :---: | :---: | :---: |
| **1** | Small Car | 30 minutes |
| **2** | Medium Car | 45 minutes |
| **3** | Large Car | 60 minutes |
| **4** | Luxury Car | 90 minutes |
| **5** | Exit | - |

For each service, the program generates a **Service Receipt** containing:

* The vehicle type.
* The time and date of **Service Start**.
* The time and date of **Estimated Delivery** (calculated automatically).
* The price charged for the service.
