---
concept: "Hall's Theorem (Halmos-Vaughn Proof)"
slug: halls-theorem-second-proof
category: matchings
subcategory: proof-techniques
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Flows, Connectivity and Matching"
chapter_number: 3
pdf_page: 74
section: "III.3 Matching"
extraction_confidence: high
aliases:
  - "second proof of Hall's theorem"
  - "Halmos-Vaughn proof"
prerequisites:
  - halls-theorem
extends: []
related: []
contrasts_with: []
answers_questions:
  - "How is Hall's theorem proved by induction?"
---

# Quick Definition
The Halmos-Vaughn proof of Hall's theorem uses induction on $m = |V_1|$, splitting into two cases: either all proper subsets have "surplus" neighbours, allowing an arbitrary first marriage; or some $k$-subset has exactly $k$ neighbours, allowing independent treatment of two parts.

# Core Definition
For $m \ge 2$: if any $k$ girls ($1 \le k < m$) know $\ge k+1$ boys, arrange one marriage arbitrarily and apply induction. If some $k$ girls know exactly $k$ boys, marry them by induction; the remaining girls still satisfy Hall's condition (since otherwise combining gives a violation) (Bollobás, p. 86).

# Prerequisites
- **Hall's theorem** — The theorem being proved

# Key Properties
1. Purely inductive proof (no flow theory)
2. Two cases based on whether surplus exists
3. The tight case ($|\Gamma(S)| = |S|$ for some $S$) is the harder case
4. Elegant and self-contained

# Context & Application
"This proof, due to Halmos and Vaughn" (p. 86), demonstrates that Hall's theorem can be proved without any reference to flows or connectivity.

# Examples
**Example** (p. 86): If 3 girls know exactly 3 boys, marry them off. The remaining girls still satisfy the condition, because if $\ell$ of them knew fewer than $\ell$ remaining boys, combining with the first 3 girls would violate the condition.

# Relationships
## Builds Upon
- **halls-theorem** — Alternative proof

# Source Reference
Chapter III, Section III.3, page 86.

# Verification Notes
- Definition source: Synthesized from proof
- Confidence rationale: Complete proof given
- Uncertainties: None
- Cross-reference status: Verified
