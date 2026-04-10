---
concept: Ackermann Function in Ramsey Theory
slug: ackermann-function
category: ramsey-theory
subcategory: null
tier: advanced
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Ramsey Theory"
chapter_number: 6
pdf_page: 209
section: "VI.4 Ramsey Theory for Integers"
extraction_confidence: high
aliases:
  - "A(p)"
  - "Ackerman's function"
prerequisites:
  - van-der-waerden-theorem
extends: []
related:
  - shelahs-theorem
contrasts_with: []
answers_questions:
  - "How fast do van der Waerden numbers grow?"
---

# Quick Definition
Ackermann's function A(p) = f_p(p), where f₁(m) = 2m and f_{n+1}(m) = f_n iterated m times starting from 1. The original proofs of van der Waerden's theorem gave bounds growing like A(p).

# Core Definition
Define f₁(m) = 2m, and f_{n+1}(m) = f_n ∘ f_n ∘ ... ∘ f_n(1) (m compositions). Then f₂(m) = 2^m, f₃(m) = tower of m 2s. **Ackermann's function** is A(p) = f_p(p). The original double-induction proofs of van der Waerden's theorem gave W(p) growing like A(p). Shelah's breakthrough reduced this to growth like f₄ (primitive recursive) (Bollobás, p. 209).

# Prerequisites
- **Van der Waerden's theorem** — Ackermann function describes its original growth rate

# Key Properties
1. f₁(m) = 2m (linear)
2. f₂(m) = 2^m (exponential)
3. f₃(m) = tower of 2s (tower function)
4. f₄ is the next level — already beyond primitive recursive for individual f_n but f₄ itself is primitive recursive
5. A(p) grows faster than any primitive recursive function

# Context & Application
Ackermann's function appears in Ramsey theory as a measure of how fast Ramsey-type functions can grow. The Van der Waerden numbers originally grew at this rate; Shelah showed they actually grow much more slowly (like f₄).

# Relationships
## Related
- **Shelah's theorem** — reduces growth from A to f₄

# Source Reference
Chapter VI: Ramsey Theory, Section VI.4, page 209.

# Verification Notes
- Definition source: Direct from p. 209
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
