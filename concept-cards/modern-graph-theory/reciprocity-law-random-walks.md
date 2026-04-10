---
concept: Reciprocity Law for Random Walks
slug: reciprocity-law-random-walks
category: random-walks
subcategory: null
tier: advanced
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Random Walks on Graphs"
chapter_number: 9
pdf_page: 317
section: "IX.3 Hitting Times and Commute Times"
extraction_confidence: high
aliases: []
prerequisites:
  - escape-probability
  - sojourn-time
extends: []
related:
  - fosters-theorem
  - mean-hitting-time
contrasts_with: []
answers_questions:
  - "How do electrical networks relate to random walks on graphs?"
---

# Quick Definition
The reciprocity law (Theorem 22) states that $d(s) P_{\text{esc}}(s \to t < u) = d(t) P_{\text{esc}}(t \to s < u)$ for any three distinct vertices $s, t, u$, and (Theorem 24) $d(s) S_x(s \to t) = d(x) S_s(x \to t)$.

# Core Definition
Theorem 22 (p. 317): "Let $s$, $t$ and $u$ be distinct vertices of a graph $G$. Then $d(s) P_{\text{esc}}(s \to t < u) = d(t) P_{\text{esc}}(t \to s < u)$." This follows from the reversibility of the random walk. Theorem 24 (p. 318): $d(s) S_x(s \to t) = d(x) S_s(x \to t)$.

# Prerequisites
- **Escape probability** — The quantity related by reciprocity
- **Sojourn time** — Related by Theorem 24

# Key Properties
1. $d(s) P_{\text{esc}}(s \to t < u) = d(t) P_{\text{esc}}(t \to s < u)$
2. $d(s) S_x(s \to t) = d(x) S_s(x \to t)$
3. Follows from reversibility: probability of traversing a walk equals probability of traversing its reverse
4. Hitting time symmetry in triples: $H(s,t) + H(t,u) + H(u,s) = H(s,u) + H(u,t) + H(t,s)$ (Theorem 23)

# Context & Application
The reciprocity law is essential for proving Foster's theorem and for showing that every network with an attachment set is equivalent to a network on that set.

# Examples
**Example** (Theorem 23, p. 318): The expected time for a round trip $s \to t \to u \to s$ equals the expected time for $s \to u \to t \to s$, by time-reversal.

# Relationships
## Builds Upon
- **escape-probability**, **sojourn-time**

## Enables
- **fosters-theorem** — First proof uses Theorem 24

# Source Reference
Chapter IX, Section IX.3, Theorems 22-24, pages 317-318.

# Verification Notes
- Definition source: Direct from Theorems 22-24
- Confidence rationale: Explicit theorems with proofs
- Uncertainties: None
- Cross-reference status: Verified
