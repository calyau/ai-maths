---
concept: Monotone Property
slug: monotone-property
category: extremal-graph-theory
subcategory: graph-properties
tier: foundational
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Extremal Problems"
chapter_number: 4
pdf_page: 110
section: "IV.3 Hamilton Paths and Cycles"
extraction_confidence: high
aliases:
  - "monotone class"
prerequisites: []
extends: []
related:
  - k-stable-property
  - k-closure
contrasts_with: []
answers_questions:
  - "What is a monotone graph property?"
---

# Quick Definition
A class of graphs is monotone if adding an edge (but no vertex) to any graph in the class keeps it in the class.

# Core Definition
A class of graphs is monotone if whenever a graph $L$ belongs to the class and $M$ is obtained from $L$ by adding an edge (but no vertex), then $M$ also belongs to the class. Most theorems in graph theory can be expressed by saying a monotone class $\mathcal{M}$ is contained in a monotone class $\mathcal{P}$ (Bollobás, p. 127).

# Prerequisites
This is a foundational concept with no prerequisites within this source.

# Key Properties
1. Closed under edge addition
2. "Containing a triangle" is a monotone property
3. "Being Hamiltonian" is a monotone property
4. A property $\mathcal{P}$ is a class closed under isomorphism

# Context & Application
Monotonicity is the framework for the Bondy-Chvátal closure approach to Hamiltonicity.

# Examples
**Example** (p. 127): $\mathcal{M} = \{G(n,m) : m > n^2/4\}$ and $\mathcal{P} = \{G : G \text{ contains a triangle}\}$ are both monotone. Turán's theorem says $\mathcal{M} \subset \mathcal{P}$.

# Relationships
## Enables
- **k-stable-property** — Stability within monotone properties
- **k-closure** — Closure operation for monotone properties

# Source Reference
Chapter IV, Section IV.3, page 127.

# Verification Notes
- Definition source: Direct from p. 127
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
