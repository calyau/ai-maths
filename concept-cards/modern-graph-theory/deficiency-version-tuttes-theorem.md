---
concept: Deficiency Version of Tutte's Theorem
slug: deficiency-version-tuttes-theorem
category: matchings
subcategory: fundamental-theorems
tier: advanced
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Flows, Connectivity and Matching"
chapter_number: 3
pdf_page: 74
section: "III.4 Tutte's 1-Factor Theorem"
extraction_confidence: high
aliases:
  - "Corollary 15"
  - "Berge's formula"
prerequisites:
  - tuttes-1-factor-theorem
extends:
  - tuttes-1-factor-theorem
related:
  - deficiency-version-halls-theorem
contrasts_with: []
answers_questions:
  - "How many vertices can be covered by a maximum matching?"
---

# Quick Definition
A graph $G$ contains a set of independent edges covering all but at most $d$ vertices iff $q(G-S) \le |S| + d$ for every $S \subset V(G)$.

# Core Definition
**Corollary 15**: A graph $G$ contains a set of independent edges covering all but at most $d$ of the vertices iff $q(G-S) \le |S| + d$ for every $S \subset V(G)$ (Bollobás, p. 93). The proof adds $d$ new vertices forming $K_d$ joined to all of $G$, then applies Tutte's theorem.

# Prerequisites
- **Tutte's 1-factor theorem** — This is the deficiency version

# Key Properties
1. Generalizes Tutte's theorem to non-perfect matchings
2. $d$ must satisfy $d \equiv |G| \pmod{2}$
3. Reduces to Tutte's theorem by adding $d$ extra vertices

# Construction / Recognition
1. Form $H = G + K_d$ (add $d$ new vertices joined to everything)
2. $H$ has a 1-factor iff the condition holds for $G$

# Context & Application
Determines the maximum matching size in general graphs.

# Examples
**Example** (p. 93): Setting $d = 0$ recovers Tutte's 1-factor theorem.

# Relationships
## Builds Upon
- **tuttes-1-factor-theorem** — Direct generalization

# Source Reference
Chapter III, Section III.4, page 93. Corollary 15.

# Verification Notes
- Definition source: Direct from p. 93
- Confidence rationale: Explicitly stated with proof
- Uncertainties: None
- Cross-reference status: Verified
