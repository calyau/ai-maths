---
# === CORE IDENTIFICATION ===
concept: Dynkin Diagram Determines Root System
slug: dynkin-determines-root-system

# === CLASSIFICATION ===
category: root-systems
subcategory: dynkin-diagrams
tier: intermediate

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Root Systems"
chapter_number: 8
pdf_page: 104
section: "8.8. Dynkin diagrams and classification of root systems"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Theorem 8.48"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - dynkin-diagram
  - cartan-matrix
  - recovery-of-root-system-from-simple-roots
extends: []
related:
  - classification-of-root-systems
  - root-system-isomorphism
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Does the Dynkin diagram determine the root system?"
  - "How does the Dynkin diagram encode root system structure?"
---

# Quick Definition
Two reduced root systems with the same Dynkin diagram are isomorphic. The Dynkin diagram determines the Cartan matrix, which determines the simple roots up to isomorphism, which determines the full root system.

# Core Definition
**Theorem 8.48** (p. 104):
1. The Dynkin diagram is connected iff $R$ is irreducible.
2. The Dynkin diagram determines the Cartan matrix $A$.
3. $R$ is determined by the Dynkin diagram uniquely up to isomorphism.

The logic: diagram $\to$ Cartan matrix (Theorem 8.48(2)) $\to$ simple roots up to isomorphism $\to$ $R$ via $R = W(\Pi)$ (Corollary 8.33).

# Prerequisites
- **dynkin-diagram** -- the data determining the root system
- **cartan-matrix** -- intermediate algebraic encoding
- **recovery-of-root-system-from-simple-roots** -- $R = W(\Pi)$

# Key Properties
1. Diagram determines Cartan matrix: edge type + arrow direction determines $a_{ij}, a_{ji}$
2. Cartan matrix determines $\Pi$ up to isomorphism
3. $\Pi$ determines $R$ via $R = W(\Pi)$
4. Therefore the Dynkin diagram is a complete invariant of the root system

# Construction / Recognition
From diagram to root system:
1. Read off Cartan matrix from diagram
2. Construct simple roots realizing this Cartan matrix
3. Generate $W$ from simple reflections
4. $R = W(\Pi)$

# Context & Application
This result, combined with Corollary 8.29 (different polarizations give $W$-conjugate $\Pi$), shows the Dynkin diagram is a well-defined invariant of the root system. It is the key step enabling the classification.

# Examples
**Example** (p. 105): $A_n$: chain of $n$ vertices with single edges uniquely determines the root system $\{e_i - e_j\}$ of $\mathfrak{sl}(n+1)$ up to isomorphism.

# Relationships
## Builds Upon
- **dynkin-diagram**, **cartan-matrix**, **recovery-of-root-system-from-simple-roots**

## Enables
- **classification-of-root-systems** -- classifying diagrams classifies root systems

## Related
- **root-system-isomorphism** -- the notion of equivalence

## Contrasts With
(none)

# Common Errors
(none)

# Common Confusions
(none)

# Source Reference
Chapter 8: Root Systems, Section 8.8, pages 104--105. Theorem 8.48.

# Verification Notes
- Definition source: Direct from Theorem 8.48
- Confidence rationale: HIGH -- explicit theorem
- Uncertainties: None
- Cross-reference status: Verified
