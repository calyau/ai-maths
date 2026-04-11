---
concept: Representation
slug: representation
category: representation-theory
subcategory: linear-representations
tier: advanced
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Representation Theory and Character Theory"
chapter_number: 18
pdf_page: 840
section: "18.1 Linear Actions and Modules over Group Rings"
extraction_confidence: high
aliases:
  - "linear representation"
  - "matrix representation"
  - "F-representation"
prerequisites:
  - group
  - vector-space
  - group-ring
extends: []
related:
  - fg-module
  - irreducible-representation
  - character
contrasts_with: []
answers_questions:
  - "What is a representation of a finite group?"
  - "What must I know before studying representation theory?"
---

# Quick Definition
A (linear) representation of a finite group G is a homomorphism φ: G → GL(V) for some vector space V over a field F. The degree is dim V. Equivalently, it is an FG-module structure on V.

# Core Definition
Let G be a finite group and F a field. A **linear representation** of G is any homomorphism φ: G → GL(V) where V is a vector space over F. The **degree** is dim V. A **matrix representation** is a homomorphism G → GL_n(F). A representation is **faithful** if injective (Definition, p. 840). Giving a representation is equivalent to giving an FG-module structure on V.

# Prerequisites
- **group** — G is a finite group
- **vector-space** — V is the representation space
- **group-ring** — FG-modules ↔ representations

# Key Properties
1. Representations ↔ FG-modules (bijective correspondence)
2. FG-submodules ↔ G-stable subspaces
3. Degree = dimension of the vector space
4. Faithful means injective (kernel is trivial)

# Examples
**Example 1** (p. 841): The trivial representation: φ(g) = I for all g. Degree 1, not faithful for |G| > 1.

**Example 2** (p. 842): The regular representation: V = FG as a left module over itself. Degree = |G|, always faithful.

**Example 3** (p. 842): S_n acts on F^n by permuting coordinates. Degree n.

# Relationships
## Enables
- **irreducible-representation** — Simple FG-modules
- **character** — The trace function of a representation

# Source Reference
Chapter 18, Section 18.1, Definition and Examples, pages 840-845.

# Verification Notes
- Confidence: HIGH — explicit definition with many examples
