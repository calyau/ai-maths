---
concept: H-Flow
slug: h-flow
category: network-flows
subcategory: algebraic-flows
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Flows"
chapter_number: 6
pdf_page: 155
section: "6.3 Group-valued flows"
extraction_confidence: high
aliases:
  - "group-valued flow"
prerequisites:
  - circulation
  - nowhere-zero-flow
extends:
  - circulation
related:
  - k-flow
  - flow-polynomial
  - flow-number
contrasts_with:
  - k-flow
answers_questions:
  - "What is a group-valued flow?"
  - "How do flows relate to abelian groups?"
---

# Quick Definition
An H-flow on a multigraph G is a nowhere-zero H-circulation: a function on directed edges valued in an abelian group H that satisfies antisymmetry, Kirchhoff's law, and is never zero.

# Core Definition
Let G = (V, E) be a multigraph and H an abelian group. An **H-flow** on G is an H-circulation that is nowhere zero, i.e., a function f: E-arrow -> H satisfying (F1), (F2), and f(e-arrow) != 0 for all e-arrow in E-arrow. (Diestel, p. 145)

For finite groups H, the number of H-flows on G depends only on |H|, not on H itself (Theorem 6.3.1, Tutte 1954). This is expressed by the flow polynomial P: the number of H-flows equals P(|H| - 1).

# Prerequisites
- **Circulation** — An H-flow is a circulation with additional requirements
- **Nowhere-zero flow** — The key additional property beyond being a circulation

# Key Properties
1. If f and g are H-circulations, f + g and -f are H-circulations, but NOT necessarily H-flows
2. A graph admitting an H-flow cannot have a bridge (Corollary 6.1.2)
3. For finite abelian groups of equal order, G has an H-flow iff G has an H'-flow (Corollary 6.3.2)
4. The number of H-flows is a polynomial in (|H| - 1)

# Context & Application
H-flows allow the use of algebraic structure in flow theory. The remarkable result that existence depends only on |H| (Corollary 6.3.2) means that crucial difficulties are unlikely to be group-theoretic in nature. Being able to choose a convenient group (e.g., Z_2^2 instead of Z_4) can simplify proofs.

# Examples
**Example** (p. 151): The Klein four-group Z_2^2 = Z_2 x Z_2 is used to prove that a graph has a 4-flow iff it is the union of two even subgraphs (Proposition 6.4.5).

# Relationships
## Builds Upon
- **Circulation** — An H-flow is a nowhere-zero circulation

## Enables
- **k-flow** — k-flows are related to Z_k-flows via Theorem 6.3.3
- **Flow polynomial** — Counts H-flows as a polynomial function

## Contrasts With
- **k-flow** — A k-flow is a Z-valued flow with |f| < k; an H-flow takes values in a general group H

# Source Reference
Chapter 6: Flows, Section 6.3, pages 145-148 (pdf pages 155-158). See Theorem 6.3.1 and Corollary 6.3.2.

# Verification Notes
- Confidence: HIGH — explicitly defined with major theorem (6.3.1) supporting it
