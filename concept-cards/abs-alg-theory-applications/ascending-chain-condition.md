---
# === CORE IDENTIFICATION ===
concept: Ascending Chain Condition
slug: ascending-chain-condition

# === CLASSIFICATION ===
category: domain-theory
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Integral Domains"
chapter_number: 18
pdf_page: 244
section: "18.2 Factorization in Integral Domains"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "ACC"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - ideal
  - integral-domain
extends: []
related:
  - noetherian-ring
  - principal-ideal-domain
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the ascending chain condition?"
  - "What is a Noetherian ring?"
---

# Quick Definition

The ascending chain condition (ACC) states that every ascending chain of ideals $I_1 \subset I_2 \subset I_3 \subset \cdots$ eventually stabilizes: there exists $N$ such that $I_n = I_N$ for all $n \geq N$.

# Core Definition

A commutative ring satisfies the ascending chain condition if for any chain of ideals $I_1 \subset I_2 \subset \cdots$, there exists $N$ such that $I_n = I_N$ for all $n \geq N$ (Judson, Lemma 18.14, p. 244). Rings satisfying the ACC are called Noetherian rings, after Emmy Noether.

# Prerequisites

- **Ideal** — The ACC concerns chains of ideals
- **Integral domain** — PIDs satisfy the ACC

# Key Properties

1. No infinite strictly ascending chains of ideals
2. Every PID satisfies the ACC (Lemma 18.14)
3. Equivalent to every ideal being finitely generated
4. Used in the proof that every PID is a UFD

# Construction / Recognition

## To Verify:
1. Show every ascending chain of ideals stabilizes
2. Or equivalently, show every ideal is finitely generated

# Context & Application

The ACC is used crucially in the proof that PIDs are UFDs: it guarantees that factorization processes terminate. The ACC defines Noetherian rings, one of the most important classes of rings in commutative algebra.

# Examples

**Example 1**: $\mathbb{Z}$ satisfies ACC since every ideal is principal ($n\mathbb{Z}$) and $n_1\mathbb{Z} \subset n_2\mathbb{Z}$ iff $n_2 | n_1$.

**Example 2**: Any PID satisfies ACC (Lemma 18.14).

# Relationships

## Enables
- **PID $\Rightarrow$ UFD** — ACC ensures factorization terminates (Theorem 18.15)
- **Noetherian ring** — Defined by ACC

## Related
- **PID** — Every PID satisfies ACC

# Common Errors

- **Error**: Confusing ACC with DCC (descending chain condition)
  **Correction**: ACC concerns ascending chains; DCC concerns descending chains (Artinian rings)

# Common Confusions

- **Confusion**: Thinking ACC means every chain is finite
  **Clarification**: The chain itself can be infinite, but it must *stabilize* (become eventually constant)

# Source Reference

Chapter 18: Integral Domains, Section 18.2, Lemma 18.14, page 244.

# Verification Notes

- Definition source: Direct from p. 244
- Confidence: HIGH — explicit definition
- Cross-reference status: Verified
- Uncertainties: None
