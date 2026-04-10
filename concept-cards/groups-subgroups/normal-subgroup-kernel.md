---
concept: Normal Subgroups as Kernels
slug: normal-subgroup-kernel
category: representations
subcategory: null
tier: intermediate
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Basic Theory of Affine Groups"
chapter_number: 1
pdf_page: 117
section: "8q Every normal affine subgroup is a kernel"
extraction_confidence: high
aliases: []
prerequisites:
  - chevalley-theorem
  - linear-representation
extends: []
related:
  - isomorphism-theorems-algebraic-groups
contrasts_with: []
answers_questions:
  - "Is every normal subgroup the kernel of a representation?"
---

# Quick Definition

Every normal subgroup N of an algebraic group G is the kernel of some representation of G. Combined with the existence of quotients, this means every normal subgroup arises as the kernel of a quotient map G -> G/N.

# Core Definition

*Theorem 8.70*: Let N be a normal subgroup of an algebraic group G. The universal surjective homomorphism G -> Q containing N in its kernel has kernel exactly N. The proof reduces to showing (Lemma 8.69) that over an algebraically closed field, N is the kernel of a representation of G. This uses Chevalley's theorem to realize N as the stabilizer of a line, then constructs a representation on which N acts trivially but nothing larger does (Milne, pp. 117-120).

# Prerequisites

- **Chevalley theorem** -- Used to realize N as a line stabilizer
- **Linear representation** -- N is realized as a kernel of a representation

# Key Properties

1. Every normal subgroup is a kernel (Theorem 8.70)
2. For distinct normal subgroups N subset N', there exists a representation on which N acts trivially but N' does not (Corollary 8.71)
3. The map N -> Rep(G)^N is a bijection from normal subgroups to certain replete subcategories (Corollary 8.76)

# Context & Application

This result validates the quotient construction for algebraic groups: every normal subgroup determines a well-defined quotient with that normal subgroup as the kernel. This is non-trivial in the algebraic group setting.

# Examples

**Example 1** (p. 118): For G = GL_n and N = SL_n (which is normal), N is the kernel of det: GL_n -> G_m.

# Relationships

## Builds Upon
- **Chevalley theorem** -- Key tool in the proof

## Enables
- **Isomorphism theorems** -- Quotients by normal subgroups are well-defined

# Source Reference

Chapter I: Basic Theory of Affine Groups, Section 8q, pages 117-120. Theorem 8.70, Lemma 8.69.

# Verification Notes

- Definition source: Direct from Theorem 8.70
- Confidence rationale: Major structural theorem
- Uncertainties: None
- Cross-reference status: Verified
