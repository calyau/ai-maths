---
concept: Field of Fractions
slug: field-of-fractions
category: ring-theory
subcategory: ring-constructions
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Introduction to Rings"
chapter_number: 7
pdf_page: 263
section: "7.5 Rings of Fractions"
extraction_confidence: high
aliases:
  - "quotient field"
  - "fraction field"
prerequisites:
  - integral-domain
  - ring-of-fractions
extends:
  - ring-of-fractions
related:
  - field
  - integral-domain
contrasts_with: []
answers_questions:
  - "What is the field of fractions of an integral domain?"
  - "How is the field of fractions related to the smallest field containing a domain?"
---

# Quick Definition
The field of fractions of an integral domain R is the field $Q = D^{-1}R$ where $D = R - \{0\}$, consisting of all "fractions" $r/s$ with $r, s \in R$ and $s \neq 0$.

# Core Definition
If R is an integral domain and $D = R - \{0\}$, the ring of fractions $Q = D^{-1}R$ is called the *field of fractions* or *quotient field* of R (Dummit & Foote, p. 263). The smallest field containing an integral domain R is its field of fractions (Corollary 16, p. 264).

# Prerequisites
- **Integral domain** — The field of fractions is defined for integral domains
- **Ring of fractions** — The construction is a special case

# Key Properties
1. Q is a field containing R as a subring
2. Every element of Q has the form $rs^{-1}$ for $r, s \in R$, $s \neq 0$
3. Q is the smallest field containing R (Corollary 16, p. 264)
4. If R is already a field, its field of fractions is R itself (p. 264)

# Construction / Recognition
## To Construct:
1. Start with an integral domain R
2. Form equivalence classes of pairs $(r, s)$ with $s \neq 0$
3. $(r, s) \sim (r', s')$ iff $rs' = r's$
4. Define arithmetic as for ordinary fractions

# Context & Application
The field of fractions is the universal way to embed an integral domain into a field, generalizing the construction of $\mathbb{Q}$ from $\mathbb{Z}$.

# Examples
**Example 1** (p. 264): The field of fractions of $\mathbb{Z}$ is $\mathbb{Q}$.

**Example 2** (p. 264): The field of fractions of the quadratic integer ring $\mathcal{O}$ is $\mathbb{Q}(\sqrt{D})$.

**Example 3** (p. 264): The field of fractions of $R[x]$ is the field of rational functions $R(x)$.

**Example 4** (p. 264): $2\mathbb{Z}$ (even integers, no identity) also has field of fractions $\mathbb{Q}$.

# Relationships

## Builds Upon
- **ring-of-fractions** — Special case with $D = R - \{0\}$

## Related
- **field** — The field of fractions is a field
- **integral-domain** — Every integral domain embeds in its field of fractions

# Common Errors
- **Error**: Assuming the field of fractions changes if we use a subring
  **Correction**: The field of fractions of $\mathbb{Z}[x]$ equals that of $\mathbb{Q}[x]$ (p. 264)

# Common Confusions
- **Confusion**: Thinking the field of fractions construction requires R to have an identity
  **Clarification**: It works for any integral domain; an identity "appears" in the field of fractions (e.g., $2\mathbb{Z}$ has no identity but $\mathbb{Q}$ does)

# Source Reference
Chapter 7, Section 7.5, Definition following Theorem 15, page 263. See Corollary 16, page 264.

# Verification Notes
- Definition: Direct from p. 263
- Confidence: HIGH — explicit definition following detailed theorem
