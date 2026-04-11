---
concept: Ascending Chain Condition on Ideals
slug: ascending-chain-condition
category: ring-theory
subcategory: structure-theorems
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Euclidean Domains, Principal Ideal Domains, and Unique Factorization Domains"
chapter_number: 8
pdf_page: 287
section: "8.3 Unique Factorization Domains (U.F.D.s)"
extraction_confidence: high
aliases:
  - "ACC"
  - "Noetherian condition"
prerequisites:
  - principal-ideal-domain
  - ideal
extends: []
related:
  - unique-factorization-domain
contrasts_with: []
answers_questions:
  - "What is the ascending chain condition on ideals?"
  - "Why does an ascending chain of ideals in a PID stabilize?"
---

# Quick Definition
A ring satisfies the ACC on ideals if every ascending chain $I_1 \subseteq I_2 \subseteq \cdots$ of ideals eventually stabilizes: $I_k = I_n$ for all $k \geq n$.

# Core Definition
Any ascending chain $I_1 \subseteq I_2 \subseteq \cdots$ of ideals in a Principal Ideal Domain eventually becomes stationary, i.e., there is some positive integer n such that $I_k = I_n$ for all $k \geq n$ (Dummit & Foote, p. 287).

# Prerequisites
- **Principal ideal domain** — PIDs satisfy ACC
- **Ideal** — The chain consists of ideals

# Key Properties
1. PIDs satisfy ACC (p. 287)
2. ACC is used to prove existence of factorizations into irreducibles in Theorem 14
3. Proof: $I = \bigcup I_i$ is an ideal; since R is a PID, $I = (a)$ for some a; then $a \in I_n$ for some n, so the chain stabilizes at $I_n$
4. More generally, rings where all ideals are finitely generated satisfy ACC (Noetherian rings)

# Context & Application
The ACC ensures that the process of factoring elements into irreducibles terminates. Without it, one might obtain infinite chains of strictly smaller factors. This is a key step in proving PIDs are UFDs.

# Source Reference
Chapter 8, Section 8.3, proof of Theorem 14, page 287.

# Verification Notes
- Definition: From proof of Theorem 14, p. 287
- Confidence: HIGH — explicit argument in the proof
