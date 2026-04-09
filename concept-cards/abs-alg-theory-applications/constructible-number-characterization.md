---
concept: Constructible Number Characterization
slug: constructible-number-characterization
category: field-theory
subcategory: geometric-constructions
tier: advanced
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Fields"
chapter_number: 21
pdf_page: 274
section: "21.3 Geometric Constructions"
extraction_confidence: high
aliases: []
prerequisites:
  - constructible-number
  - tower-theorem
extends: []
related:
  - doubling-the-cube
  - trisecting-an-angle
contrasts_with: []
answers_questions:
  - "What is the algebraic characterization of constructible numbers?"
---

# Quick Definition

A real number $\alpha$ is constructible if and only if there exists a tower of fields $\mathbb{Q} = F_0 \subset F_1 \subset \cdots \subset F_k$ with $F_i = F_{i-1}(\sqrt{\alpha_i})$ and $\alpha \in F_k$. This forces $[\mathbb{Q}(\alpha):\mathbb{Q}]$ to be a power of 2.

# Core Definition

**Theorem 21.43.** A real number $\alpha$ is a constructible number if and only if there exists a sequence of fields $\mathbb{Q} = F_0 \subset F_1 \subset \cdots \subset F_k$ such that $F_i = F_{i-1}(\sqrt{\alpha_i})$ with $\alpha_i \in F_i$ and $\alpha \in F_k$. In particular, there exists an integer $k > 0$ such that $[\mathbb{Q}(\alpha):\mathbb{Q}] = 2^k$ (Judson, p. 287).

# Prerequisites

- **Constructible number** — The geometric definition
- **Tower theorem** — Used to compute the total degree

# Key Properties

1. Each step is a quadratic extension ($[F_i:F_{i-1}] = 2$)
2. The total degree is $[F_k:\mathbb{Q}] = 2^k$
3. If $[\mathbb{Q}(\alpha):\mathbb{Q}]$ is not a power of 2, $\alpha$ is not constructible
4. The converse direction follows from the fact that straightedge-compass intersections solve at most quadratic equations (Lemma 21.42)

# Context & Application

This characterization transforms geometric construction problems into algebraic degree computations. The power-of-2 condition is the key tool for all impossibility proofs.

# Examples

**Example 1** (p. 287): $\sqrt[3]{2}$ has $[\mathbb{Q}(\sqrt[3]{2}):\mathbb{Q}] = 3 \neq 2^k$, so it is not constructible.

**Example 2** (p. 288): $\cos 20°$ has $[\mathbb{Q}(\cos 20°):\mathbb{Q}] = 3 \neq 2^k$, so it is not constructible.

# Relationships

## Builds Upon
- **Constructible number** — Algebraic characterization of the geometric concept
- **Tower theorem** — Computes the total degree

## Enables
- **Doubling the cube** — Impossibility follows from degree 3
- **Trisecting an angle** — Impossibility follows from degree 3

# Source Reference

Chapter 21: Fields, Section 21.3, pages 287–288. Theorem 21.43.

# Verification Notes

- Definition source: Direct from Theorem 21.43, p. 287
- Confidence: HIGH — explicit theorem
- Cross-reference status: Verified
- Uncertainties: None
