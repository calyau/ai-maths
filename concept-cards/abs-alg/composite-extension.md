---
concept: Composite Extension
slug: composite-extension
category: galois-theory
subcategory: composite-extensions
tier: advanced
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Galois Theory"
chapter_number: 14
pdf_page: 592
section: "14.4 Composite Extensions and Simple Extensions"
extraction_confidence: high
aliases:
  - "compositum"
  - "composite of fields"
prerequisites:
  - field-extension
  - galois-extension
extends: []
related:
  - simple-extension
contrasts_with: []
answers_questions:
  - "What is a composite extension?"
---

# Quick Definition
The composite (or compositum) of field extensions $K_1$ and $K_2$ inside an ambient field L is the smallest subfield of L containing both $K_1$ and $K_2$, denoted $K_1 K_2$.

# Core Definition
If $K_1$ and $K_2$ are subfields of a field L, their composite $K_1 K_2$ is the smallest subfield of L containing both. If $K_1/F$ and $K_2/F$ are Galois, then $K_1 K_2/F$ is Galois. The Galois group $\text{Gal}(K_1 K_2/F)$ embeds in $\text{Gal}(K_1/F) \times \text{Gal}(K_2/F)$, with equality when $K_1 \cap K_2 = F$ (Dummit & Foote, pp. 592-597).

# Prerequisites
- **field-extension**, **galois-extension**

# Key Properties
1. $K_1 K_2$ is the smallest field containing both $K_1$ and $K_2$
2. If $K_1 \cap K_2 = F$: $[K_1 K_2:F] = [K_1:F][K_2:F]$
3. Galois composite of Galois extensions is Galois
4. If $K_1 \cap K_2 = F$ and both Galois: $\text{Gal}(K_1 K_2/F) \cong \text{Gal}(K_1/F) \times \text{Gal}(K_2/F)$

# Relationships
## Builds Upon
- **field-extension**, **galois-extension**

## Related
- **simple-extension** — A composite of simple extensions

# Source Reference
Chapter 14, Section 14.4, pp. 592-597.

# Verification Notes
- Confidence: HIGH — explicit definition with Galois theory results
