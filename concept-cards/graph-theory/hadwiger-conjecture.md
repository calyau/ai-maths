---
concept: "Hadwiger's Conjecture"
slug: hadwiger-conjecture
category: extremal-graph-theory
subcategory: minors
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Extremal Graph Theory"
chapter_number: 7
pdf_page: 183
section: "7.3 Hadwiger's conjecture"
extraction_confidence: high
aliases:
  - "Hadwiger conjecture"
prerequisites:
  - graph
  - kostochka-theorem
related:
  - turan-theorem
  - four-colour-theorem
  - girth-forcing-minors
  - wagner-theorem
answers_questions:
  - "What is Hadwiger's conjecture?"
  - "How does chromatic number relate to graph minors?"
---

# Quick Definition
Hadwiger's conjecture (1943) states that chi(G) >= r implies G contains K^r as a minor, for every integer r > 0 and every graph G.

# Core Definition
**Conjecture** (Hadwiger 1943): The following implication holds for every integer r > 0 and every graph G:

chi(G) >= r => G >= K^r (G has K^r as a minor).

The conjecture is trivial for r <= 2, easy for r = 3 and r = 4, equivalent to the four colour theorem for r = 5 and r = 6, and open for r >= 7. (Diestel, pp. 172-176)

# Prerequisites
- **Graph** — The conjecture is about all graphs
- **Kostochka's theorem** — Provides context: cr*sqrt(log r) average degree forces K^r minor

# Key Properties
1. Viewed by many as the most challenging open problem in graph theory
2. Can be viewed as a generalization of the four colour theorem
3. Status by r: trivial (r <= 2), easy (r = 3,4), depends on 4CT (r = 5,6), open (r >= 7)
4. True for line graphs, large-girth graphs, and "almost all" graphs
5. The conjecture for r+1 implies it for r
6. Rephrased: every graph without K^r minor is (r-1)-colourable

# Context & Application
Hadwiger's conjecture asks whether the chromatic number chi has a direct structural effect beyond merely implying high average degree. The question is whether chi(G) >= r forces a K^r minor more efficiently than the average degree of d(G) >= r-1 (which it implies). So far, no proof technique is known that exploits the full power of the chromatic number assumption.

# Examples
**Example** (p. 173): For r = 3, graphs without K^3 minor are forests, which are 2-colourable.
**Example** (p. 173, Proposition 7.3.1): For r = 4, edge-maximal graphs without K^4 minor are built from triangles by pasting along K^2s, and are 3-colourable.

# Relationships
## Related
- **Four colour theorem** — Hadwiger's conjecture for r = 5,6 is equivalent to the 4CT
- **Wagner's theorem** — Structure of graphs without K^5 minor (Theorem 7.3.4)
- **Kostochka's theorem** — Best unconditional bound via average degree

# Common Confusions
- **Confusion**: Confusing Hadwiger's conjecture with Hajos's conjecture
  **Clarification**: Hadwiger concerns general minors (K^r minor); Hajos concerns topological minors (TK^r). Hajos's conjecture is false in general.

# Source Reference
Chapter 7, Section 7.3, pages 172-176 (pdf pages 183-186). Proposition 7.3.1, Theorem 7.3.4, Theorem 7.3.7.

# Verification Notes
- Confidence: HIGH — named conjecture, extensively discussed with partial results
