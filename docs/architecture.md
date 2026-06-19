# AI Technical Mentor - Architecture (Version 1)

## 1. Purpose

This document describes the architecture for Version 1 (MVP) of AI Technical Mentor.

The goal of Version 1 is to perform a Diagnostic Assessment that helps users understand their current strengths, weaknesses, and learning gaps relative to a target technical role.

Version 1 intentionally focuses on assessment and feedback only.

Features such as learner memory, personalized roadmaps, RAG, and agent-based workflows are out of scope for this version.

---

## 2. Version 1 Goals

The system should allow a user to:

1. Select a target role.
2. Complete a diagnostic assessment.
3. Receive personalized feedback.
4. Understand strengths and weaknesses.
5. Receive recommended topics for improvement.

---

## 3. High-Level Architecture


```text
+--------------------+
| Angular Frontend   |
+--------------------+
          |
          |
          v
+--------------------+
| FastAPI Backend    |
+--------------------+
          |
          |
          v
+--------------------+
| OpenAI API         |
+--------------------+
```

---

## 4. Component Responsibilities

### Angular Frontend

Responsibilities:

* Capture user inputs
* Display assessment questions
* Capture user responses
* Display assessment results
* Display strengths and weaknesses
* Display recommended learning topics

The frontend should not contain AI-specific business logic.

---

### FastAPI Backend

Responsibilities:

* Manage assessment sessions
* Generate assessment questions
* Evaluate user responses
* Track assessment progress
* Generate assessment reports

The backend acts as the orchestration layer between the frontend and OpenAI.

---

### OpenAI API

Responsibilities:

* Generate diagnostic questions
* Evaluate user answers
* Identify strengths and weaknesses
* Generate assessment summaries

---

## 5. User Journey

### Step 1

User selects a target role.

Example:

* AI Application Engineer
* Python Developer
* Senior Java Developer
* Full Stack Developer

---

### Step 2

System starts a Diagnostic Assessment.

The backend generates role-specific assessment questions.

---

### Step 3

User answers questions.

The backend stores responses for the active session.

---

### Step 4

The system evaluates responses.

Evaluation criteria:

* Correctness
* Completeness
* Clarity
* Technical Understanding

---

### Step 5

Assessment Report is generated.

Report includes:

* Overall Score
* Strengths
* Weaknesses
* Recommended Learning Topics

---

## 6. API Design

### Start Assessment

```http
POST /assessment/start
```

Request:

```json
{
  "target_role": "AI Application Engineer"
}
```

Response:

```json
{
  "session_id": "123",
  "question": "Explain Retrieval-Augmented Generation (RAG)."
}
```

---

### Submit Answer

```http
POST /assessment/answer
```

Request:

```json
{
  "session_id": "123",
  "answer": "RAG combines retrieval and generation..."
}
```

Response:

```json
{
  "score": 7,
  "feedback": "Good answer but missing retrieval pipeline details.",
  "next_question": "What are vector embeddings?"
}
```

---

### Finish Assessment

```http
POST /assessment/finish
```

Response:

```json
{
  "overall_score": 6.5,
  "strengths": [
    "Backend Development",
    "REST APIs"
  ],
  "weaknesses": [
    "Embeddings",
    "Vector Databases"
  ],
  "recommended_topics": [
    "RAG",
    "Embeddings",
    "Vector Search"
  ]
}
```

---

## 7. Backend Folder Structure

```text
backend/

app/
│
├── api/
│   └── assessment.py
│
├── services/
│   ├── question_service.py
│   ├── evaluation_service.py
│   └── report_service.py
│
├── prompts/
│   ├── question_prompt.txt
│   ├── evaluation_prompt.txt
│   └── report_prompt.txt
│
├── models/
│   ├── requests.py
│   └── responses.py
│
├── config.py
│
└── main.py
```

---

## 8. Session Management

Version 1 does not persist data.

Assessment data is maintained only for the duration of the active assessment session.

Future versions may introduce:

* Database storage
* Learner profiles
* Progress tracking
* Long-term memory

---

## 9. Future Evolution

### Version 2

* CV Upload
* CV Analysis
* Skill Gap Analysis
* Personalized Learning Roadmaps

### Version 3

* Learner Profile
* Interview History
* Progress Tracking
* Adaptive Assessments

### Version 4

* Knowledge Base (RAG)
* PDF Uploads
* Notes Uploads
* Personalized Retrieval

### Version 5

* Agent-Based Mentoring
* Adaptive Coaching
* Career Readiness Evaluation

---

## 10. Design Principles

1. Start simple.
2. Build working software quickly.
3. Introduce complexity only when justified.
4. Focus on user value over technical complexity.
5. Use AI to support mentorship, not just evaluation.

---

## 11. Version 1 Success Criteria

Version 1 is successful if a user can:

* Start a diagnostic assessment.
* Complete an assessment session.
* Receive useful feedback.
* Understand strengths and weaknesses.
* Identify topics that require improvement.

```
```
