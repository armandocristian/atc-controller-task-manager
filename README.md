# Proiect DevOps - Aplicație To-Do pentru Managementul task-urilor controlorilor de trafic aerian

## Descriere

Acest proiect prezintă implementarea unui flux DevOps complet pentru o aplicație web dezvoltată în Python (Flask), destinată gestionării zborurilor și controlorilor de trafic aerian (ATC).

Scopul proiectului este automatizarea procesului de integrare, testare, construire, livrare și monitorizare a aplicației utilizând tehnologii moderne DevOps.

---

# Repository

**GitHub Repository**

https://github.com/armandocristian/atc-controller-task-manager

**Docker Hub**

https://hub.docker.com/repository/docker/armandopopa/atc-todo-app/general

---

# Arhitectura soluției

Fluxul complet al aplicației este prezentat mai jos:

```
                    Developer
                        │
                        ▼
                 GitHub Repository
                        │
                 GitHub Webhook
                        │
                        ▼
                 Jenkins Pipeline
                        │
      ┌─────────────────┼─────────────────┐
      │                 │                 │
      ▼                 ▼                 ▼
 Checkout      Install Dependencies    Run Tests
      │
      ▼
 Build Docker Image
      │
      ▼
 Push Docker Image (Docker Hub)
      │
      ▼
 Deploy în Kubernetes
      │
      ▼
  Aplicația Flask
      │
      ├───────────────┐
      ▼               ▼
 Prometheus       Grafana
```

---

# Tehnologii utilizate

- Python 3
- Flask
- Pytest
- Git
- GitHub
- Jenkins
- Docker
- Docker Hub
- Kubernetes (Kind)
- kubectl
- Helm
- Prometheus
- Grafana
- Ubuntu Linux

---

# Structura proiectului

```
.
├── backend/
├── tests/
├── k8s/
│   ├── namespace.yaml
│   ├── deployment.yaml
│   └── service.yaml
├── screenshots/
├── Dockerfile
├── Jenkinsfile
├── requirements.txt
├── docker-compose.yml
└── README.md
```

---

# Cerințe

# Cerințe preliminare (Prerequisites)

Pentru rularea proiectului sunt necesare următoarele componente:

- Ubuntu 22.04 LTS (sau o distribuție Linux compatibilă)
- Git
- Python 3
- pip
- Docker Engine
- Kubernetes (Kind)
- kubectl
- Helm
- Jenkins
- ngrok
- Cont GitHub
- Cont Docker Hub




---

# Instalare

## 1. Clonarea repository-ului

```bash
git clone https://github.com/armandocristian/atc-controller-task-manager.git
cd atc-controller-task-manager
```

## 2. Instalarea dependențelor

```bash
pip install -r requirements.txt
```

## 3. Construirea imaginii Docker

```bash
docker build -t armandopopa/atc-todo-app:1.0 .
```

## 4. Publicarea imaginii în Docker Hub

```bash
docker push armandopopa/atc-todo-app:1.0
```

---

# Rularea aplicației în Kubernetes

Crearea resurselor:

```bash
kubectl apply -f k8s/
```

Verificarea podurilor:

```bash
kubectl get pods -n atc
```

Verificarea serviciului:

```bash
kubectl get svc -n atc
```

Accesarea aplicației:

```bash
kubectl port-forward -n atc service/atc-todo-service 5000:5000
```

Aplicația este disponibilă la:

```
http://localhost:5000
```

---

# Pipeline CI/CD

Pipeline-ul Jenkins automatizează întregul proces de integrare și livrare continuă.

Etapele executate sunt:

- Checkout cod sursă din GitHub
- Instalarea dependențelor
- Rularea testelor automate (Pytest)
- Construirea imaginii Docker
- Publicarea imaginii în Docker Hub
- Deploy automat în Kubernetes
- Rolling Update al aplicației

Pipeline-ul este declanșat automat prin GitHub Webhook la fiecare modificare trimisă în repository.

---

# Monitorizare

Monitorizarea infrastructurii și a aplicației este realizată folosind:

- Prometheus
- Grafana

Prometheus colectează metrici despre infrastructura Kubernetes și aplicație.

Grafana afișează aceste metrici prin dashboard-uri interactive care monitorizează:

- utilizarea procesorului;
- utilizarea memoriei;
- utilizarea discului;
- starea podurilor Kubernetes;
- funcționarea serviciilor.

---

# Logging

Logurile aplicației pot fi vizualizate utilizând:

```bash
kubectl logs -n atc deployment/atc-todo-app
```

Acestea permit monitorizarea cererilor HTTP și identificarea eventualelor probleme în timpul rulării aplicației.

---

# Capturi de ecran

Directorul **screenshots/** conține capturi care demonstrează funcționarea proiectului:

- GitHub Repository
- Jenkins Pipeline
- Jenkins Console Output
- Docker Hub
- Kubernetes
- Aplicația Flask
- Prometheus
- Grafana
- Application Logs


---

# Rezultate obținute

În cadrul proiectului au fost implementate următoarele funcționalități:

- integrarea codului sursă în GitHub;
- automatizarea procesului CI/CD folosind Jenkins;
- containerizarea aplicației folosind Docker;
- publicarea imaginilor în Docker Hub;
- orchestrarea containerelor în Kubernetes;
- monitorizarea infrastructurii folosind Prometheus și Grafana;
- integrarea GitHub Webhook cu Jenkins pentru declanșarea automată a pipeline-ului.

---

# Posibile îmbunătățiri


- integrarea unei soluții centralizate de logare (ELK Stack sau Grafana Loki);
- deployment într-un mediu cloud (AWS, Azure sau Google Cloud);
- integrarea scanării vulnerabilităților și analizelor statice de cod în pipeline.

---

# Autor

**Cristian Popa**

Proiect realizat în cadrul cursului DevOps.
