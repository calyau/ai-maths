---
# === CORE IDENTIFICATION ===
concept: Dynkin Diagram
slug: dynkin-diagram

# === CLASSIFICATION ===
category: root-systems
subcategory: dynkin-diagrams
tier: foundational

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
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - simple-roots
  - cartan-matrix
  - root-angles-and-length-ratios
extends: []
related:
  - classification-of-root-systems
  - reducible-root-system
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a Dynkin diagram?"
  - "How do Dynkin diagrams encode root system structure?"
  - "How do I construct the Dynkin diagram from a root system?"
---

# Quick Definition
The Dynkin diagram of a root system is a graph with one vertex per simple root, edges encoding the angles between pairs (0, 1, 2, or 3 edges for angles $\pi/2$, $2\pi/3$, $3\pi/4$, $5\pi/6$), and arrows on multiple edges pointing toward the shorter root. It determines the root system up to isomorphism.

# Core Definition
The Dynkin diagram of a set of simple roots $\Pi$ is constructed as follows (Definition 8.46, p. 104):

1. For each simple root $\alpha_i$, draw a vertex $v_i$
2. For each pair $\alpha_i \neq \alpha_j$, connect $v_i$ and $v_j$ by $n$ edges where $n$ depends on the angle $\varphi$ between them:
   - $\varphi = \pi/2$: $n = 0$ (no edge)
   - $\varphi = 2\pi/3$: $n = 1$
   - $\varphi = 3\pi/4$: $n = 2$
   - $\varphi = 5\pi/6$: $n = 3$
3. For non-orthogonal roots of different lengths, place an arrow on the multiple edge pointing toward the shorter root

# Prerequisites
- **simple-roots** -- one vertex per simple root
- **cartan-matrix** -- equivalent algebraic encoding
- **root-angles-and-length-ratios** -- determines edge multiplicity

# Key Properties
1. The Dynkin diagram is connected iff $R$ is irreducible (Theorem 8.48(1))
2. The Dynkin diagram determines the Cartan matrix (Theorem 8.48(2))
3. The root system is determined up to isomorphism by the Dynkin diagram (Theorem 8.48(3))
4. Number of vertices equals $r = \operatorname{rank}(R)$
5. The number of edges between vertices $i,j$ equals $a_{ij}a_{ji}$ (where $a_{ij}$ is the Cartan matrix entry)

# Construction / Recognition
## To construct the Dynkin diagram from simple roots
1. Draw one vertex per simple root
2. For each pair $i \neq j$, compute $a_{ij}a_{ji} = 4\cos^2\varphi$
3. Draw $a_{ij}a_{ji}$ edges between $v_i$ and $v_j$
4. If $a_{ij}a_{ji} > 0$ and $|\alpha_i| \neq |\alpha_j|$, add an arrow pointing to the shorter root

## To recover the Cartan matrix from the diagram
1. $a_{ii} = 2$ always
2. No edge: $a_{ij} = a_{ji} = 0$
3. Single edge: $a_{ij} = a_{ji} = -1$
4. Double edge, arrow $i \to j$: $a_{ij} = -1$, $a_{ji} = -2$
5. Triple edge, arrow $i \to j$: $a_{ij} = -1$, $a_{ji} = -3$

# Context & Application
Dynkin diagrams are the culminating tool of Chapter 8. The classification of all reduced irreducible root systems (and hence all simple Lie algebras) reduces to classifying connected Dynkin diagrams. The visual simplicity of diagrams makes the classification memorable and computable.

# Examples
**Example 8.47** (p. 104): Rank two Dynkin diagrams (Figure 8.5):
- $A_1 \times A_1$: two disconnected vertices
- $A_2$: two vertices, single edge
- $B_2$: two vertices, double edge with arrow
- $G_2$: two vertices, triple edge with arrow

# Relationships
## Builds Upon
- **cartan-matrix** -- equivalent encoding
- **simple-roots** -- vertices correspond to simple roots
- **root-angles-and-length-ratios** -- determines edges

## Enables
- **classification-of-root-systems** -- reduces to classifying Dynkin diagrams

## Related
- **reducible-root-system** -- disconnected diagram

## Contrasts With
(none)

# Common Errors
- **Error**: Forgetting the arrow direction on multiple edges
  **Correction**: Arrow points to the shorter root; without the arrow, information about which root is shorter is lost

- **Error**: Drawing an arrow on a single edge (where both roots have equal length)
  **Correction**: Single edges never have arrows; they connect roots of equal length

# Common Confusions
- **Confusion**: Thinking the number of edges equals $|a_{ij}|$
  **Clarification**: The number of edges equals $a_{ij}a_{ji}$, not $|a_{ij}|$; for single edges $a_{ij} = a_{ji} = -1$ so $a_{ij}a_{ji} = 1$

# Source Reference
Chapter 8: Root Systems, Section 8.8, pages 104--105. Definition 8.46, Example 8.47, Theorem 8.48.

# Verification Notes
- Definition source: Direct from Definition 8.46
- Confidence rationale: HIGH -- explicit construction with examples
- Uncertainties: None
- Cross-reference status: Verified
