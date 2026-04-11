---
concept: Domain Hierarchy
slug: domain-hierarchy
category: ring-theory
subcategory: structure-theorems
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Euclidean Domains, Principal Ideal Domains, and Unique Factorization Domains"
chapter_number: 8
pdf_page: 290
section: "8.3 Unique Factorization Domains (U.F.D.s)"
extraction_confidence: high
aliases:
  - "chain of domain types"
prerequisites:
  - field
  - euclidean-domain
  - principal-ideal-domain
  - unique-factorization-domain
  - integral-domain
extends: []
related: []
contrasts_with: []
answers_questions:
  - "How do Euclidean domains, PIDs, and UFDs relate to each other?"
---

# Quick Definition
Fields $\subset$ Euclidean Domains $\subset$ PIDs $\subset$ UFDs $\subset$ integral domains, with all inclusions proper.

# Core Definition
The following inclusions hold among classes of commutative rings with identity, all containments being proper: fields $\subset$ Euclidean Domains $\subset$ P.I.D.s $\subset$ U.F.D.s $\subset$ integral domains (Dummit & Foote, p. 290).

# Prerequisites
- **Field** — The most structured class
- **Euclidean domain** — Has a division algorithm
- **Principal ideal domain** — Every ideal is principal
- **Unique factorization domain** — Has unique factorization
- **Integral domain** — No zero divisors

# Key Properties
1. $\mathbb{Z}$ is Euclidean but not a field
2. $\mathbb{Z}[(1+\sqrt{-19})/2]$ is a PID but not Euclidean
3. $\mathbb{Z}[x]$ is a UFD but not a PID
4. $\mathbb{Z}[\sqrt{-5}]$ is an integral domain but not a UFD
5. The UFD property passes to polynomial rings; PID and Euclidean do not

# Context & Application
This hierarchy summarizes the main structural results of Chapter 8 and provides the classification framework for commutative rings with identity.

# Source Reference
Chapter 8, Section 8.3, Summary, page 290.

# Verification Notes
- Definition: Direct summary from p. 290
- Confidence: HIGH — explicit summary with examples for each gap
