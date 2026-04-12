---
concept: "Schur's Lemma"
slug: schurs-lemma
category: group-representations
subcategory: null
tier: advanced
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Group Representations"
chapter_number: 10
pdf_page: 301
section: "10.7 Schur's Lemma"
extraction_confidence: high
aliases: []
prerequisites: [irreducible-representation]
extends: []
related: [orthogonality-of-characters]
contrasts_with: []
answers_questions: ["What is Schur's lemma?"]
---
# Quick Definition
Schur's Lemma states: (a) a G-invariant linear map between irreducible representations is either zero or an isomorphism, and (b) a G-invariant linear operator on an irreducible representation is a scalar multiple of the identity.
# Core Definition
Theorem 10.7.6 (Schur's Lemma): (a) Let rho, rho' be irreducible representations on V, V'. If T: V' -> V is G-invariant, then either T is an isomorphism or T = 0. (b) Let rho be irreducible on V. If T: V -> V is G-invariant, then T = cI for some scalar c (Artin, p. 321).
# Prerequisites
- **Irreducible representation** — Schur's Lemma applies to irreducible representations
# Key Properties
1. Part (a): G-invariant maps between irreducibles are "all or nothing"
2. Part (b): The only G-invariant operators on an irreducible space are scalars
3. Proof of (a): ker T and im T are G-invariant subspaces; irreducibility forces them to be trivial or everything
4. Proof of (b): T - lambda I is G-invariant and has nontrivial kernel (lambda is an eigenvalue), so by (a) it must be zero
5. Schur's Lemma is the basis for proving the orthogonality relations
# Construction / Recognition
## To Apply:
1. Verify both representations are irreducible
2. Check T is G-invariant: T(gv) = gT(v)
3. Conclude T = 0 or T is an isomorphism (part a), or T = cI (part b)
# Context & Application
Schur's Lemma is the technical engine behind the orthogonality relations and the Main Theorem on characters. The averaging process (10.7.7) creates G-invariant maps from arbitrary maps, and Schur's Lemma then determines what these averaged maps can be.
# Examples
**Example 1** (p. 321): If rho and rho' are non-isomorphic irreducible representations, the averaged G-invariant map T-tilde must be zero by Schur's Lemma.
# Relationships
## Builds Upon
- **Irreducible representation** — Required hypothesis
## Enables
- **Orthogonality of characters** — Proved using Schur's Lemma and averaging
# Common Errors
- **Error**: Applying Schur's Lemma to reducible representations
  **Correction**: Both representations must be irreducible for the lemma to apply
# Source Reference
Chapter 10: Group Representations, Section 10.7, Theorem 10.7.6, pages 320-322.
# Verification Notes
- Definition source: Direct from Theorem 10.7.6
- Confidence rationale: Major lemma, fully proved
- Uncertainties: None
- Cross-reference status: Verified
