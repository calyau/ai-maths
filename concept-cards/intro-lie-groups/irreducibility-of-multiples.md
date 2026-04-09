---
# === CORE IDENTIFICATION ===
concept: Only Multiples of a Root are Plus or Minus
slug: irreducibility-of-multiples

# === CLASSIFICATION ===
category: root-systems
subcategory: abstract-root-systems
tier: intermediate

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Complex Semisimple Lie Algebras"
chapter_number: 7
pdf_page: 88
section: "7.3. Root decomposition and root systems"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "reduced property of roots"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - root
  - sl2-subalgebra-of-root
extends: []
related:
  - structure-theorem-roots
  - reduced-root-system
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Can 2*alpha be a root if alpha is a root?"
---

# Quick Definition

If $\alpha$ is a root, then the only multiples of $\alpha$ that are also roots are $\pm\alpha$. In particular, $2\alpha$ is never a root. This "reduced" property follows from the irreducible $\mathfrak{sl}(2)_\alpha$ representation structure.

# Core Definition

**Theorem 7.21, part (5)** (Kirillov, p. 88): For any root $\alpha$, the only multiples of $\alpha$ which are also roots are $\pm\alpha$.

# Prerequisites

- **Root** — The property concerns roots
- **sl(2) subalgebra of a root** — The proof uses the irreducible representation $V = \mathbb{C}h_\alpha \oplus \bigoplus_{k \neq 0} \mathfrak{g}_{k\alpha}$

# Key Properties

1. The proof shows $c$ must be a half-integer with $1/c$ also a half-integer, giving $c \in \{\pm 1, \pm 2, \pm 1/2\}$
2. Then Lemma 7.20 shows $V$ has highest weight 2 (since $\mathfrak{g}_\alpha$ is 1-dimensional and $\operatorname{ad} e_\alpha\colon \mathfrak{g}_\alpha \to \mathfrak{g}_{2\alpha}$ is zero)
3. Therefore $V = \mathfrak{g}_{-\alpha} \oplus \mathbb{C}h_\alpha \oplus \mathfrak{g}_\alpha$, so $\mathfrak{g}_{2\alpha} = 0$

# Context & Application

This result ensures the root system of a semisimple Lie algebra is always "reduced" in the sense of abstract root system theory. Non-reduced root systems (like $BC_n$) do not arise from semisimple algebras.

# Relationships

## Related
- **Reduced root system** — This property is the "reduced" axiom

# Source Reference

Chapter 7: Complex Semisimple Lie Algebras, Section 7.3, page 88. Theorem 7.21(5).

# Verification Notes

- Definition source: Direct from Theorem 7.21(5)
- Confidence rationale: Explicit theorem part with proof
- Uncertainties: None
- Cross-reference status: Verified
