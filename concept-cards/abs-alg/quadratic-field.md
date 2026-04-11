---
concept: Quadratic Field
slug: quadratic-field
category: ring-theory
subcategory: ring-constructions
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Introduction to Rings"
chapter_number: 7
pdf_page: 227
section: "7.1 Basic Definitions and Examples"
extraction_confidence: high
aliases: []
prerequisites:
  - field
extends:
  - field
related:
  - quadratic-integer-ring
  - field-of-fractions
contrasts_with: []
answers_questions:
  - "What is a quadratic field?"
---

# Quick Definition
The quadratic field $\mathbb{Q}(\sqrt{D})$ for squarefree integer D is $\{a + b\sqrt{D} \mid a, b \in \mathbb{Q}\}$, a subfield of $\mathbb{C}$.

# Core Definition
Let D be a squarefree integer. The quadratic field $\mathbb{Q}(\sqrt{D}) = \{a + b\sqrt{D} \mid a, b \in \mathbb{Q}\}$ is a field (subring of $\mathbb{C}$, or of $\mathbb{R}$ if $D > 0$). It is the field of fractions of the quadratic integer ring $\mathcal{O}$ (Dummit & Foote, pp. 227-228).

# Prerequisites
- **Field** — $\mathbb{Q}(\sqrt{D})$ is a field

# Key Properties
1. Every nonzero element has an inverse: $(a + b\sqrt{D})^{-1} = \frac{a - b\sqrt{D}}{a^2 - Db^2}$ (since $a^2 - Db^2 \neq 0$ when D is not a perfect square)
2. $\mathbb{Q}(\sqrt{D}) = \mathbb{Q}(\sqrt{D'})$ where $D'$ is the squarefree part of D
3. The ring of integers $\mathcal{O}$ in $\mathbb{Q}(\sqrt{D})$ has $\mathbb{Q}(\sqrt{D})$ as its field of fractions

# Examples
**Example 1**: $\mathbb{Q}(\sqrt{-1}) = \mathbb{Q}(i) = \{a + bi \mid a, b \in \mathbb{Q}\}$.

**Example 2**: $\mathbb{Q}(\sqrt{2}) = \{a + b\sqrt{2} \mid a, b \in \mathbb{Q}\} \subset \mathbb{R}$.

# Source Reference
Chapter 7, Section 7.1, Example (5), pages 227-228.

# Verification Notes
- Definition: Direct from pp. 227-228
- Confidence: HIGH — explicit construction
