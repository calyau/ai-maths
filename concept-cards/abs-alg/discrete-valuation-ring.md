---
concept: Discrete Valuation Ring
slug: discrete-valuation-ring
category: commutative-algebra
subcategory: valuation-theory
tier: advanced
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Artinian Rings, Discrete Valuation Rings, and Dedekind Domains"
chapter_number: 16
pdf_page: 757
section: "16.2 Discrete Valuation Rings"
extraction_confidence: high
aliases:
  - "DVR"
  - "D.V.R."
prerequisites:
  - discrete-valuation
  - pid
extends:
  - pid
related:
  - local-ring
  - dedekind-domain
contrasts_with: []
answers_questions:
  - "What is a discrete valuation ring?"
---

# Quick Definition
A DVR is an integral domain that is the valuation ring of a discrete valuation on its fraction field. Equivalently, it is a PID with a unique maximal ideal, or a Noetherian integrally closed local domain of Krull dimension 1.

# Core Definition
An integral domain R is a **Discrete Valuation Ring (DVR)** if R is the valuation ring of a discrete valuation ν on its fraction field (Definition, p. 757). By Theorem 7 (p. 760), the following are equivalent: (1) R is a DVR, (2) R is a PID with a unique maximal ideal ≠ 0, (3) R is a UFD with a unique irreducible element t, (4) R is a Noetherian local domain with a nonzero principal maximal ideal, (5) R is a Noetherian integrally closed local domain of Krull dimension 1.

# Prerequisites
- **discrete-valuation** — DVRs are valuation rings
- **pid** — DVRs are PIDs

# Key Properties
1. Every nonzero ideal is (t^n) for some n ≥ 0 (Proposition 5)
2. Spec R = {0, M} where M = (t) is the unique maximal ideal
3. A nonzero element u is a unit iff ν(u) = 0
4. Every element is ut^n for some unit u and n ≥ 0
5. DVRs are Euclidean domains, hence PIDs and UFDs

# Examples
**Example** (p. 757): Z_(p) is a DVR with valuation v_p and uniformizer p.

**Example** (p. 758): F[x]_(f) for irreducible f is a DVR; the formal power series ring F[[x]] is a DVR.

# Relationships
## Builds Upon
- **pid** — DVRs are PIDs with unique maximal ideal

## Enables
- **dedekind-domain** — Localizations of Dedekind domains at nonzero primes are DVRs

# Source Reference
Chapter 16, Section 16.2, Definition, Proposition 5, Theorem 7, pages 757-762.

# Verification Notes
- Confidence: HIGH — five equivalent characterizations given
