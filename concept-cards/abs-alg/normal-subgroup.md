---
concept: Normal Subgroup
slug: normal-subgroup
category: group-theory
subcategory: quotients
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Quotient Groups and Homomorphisms"
chapter_number: 3
pdf_page: 73
section: "3.1 Definitions and Examples"
extraction_confidence: high
aliases:
  - "$N \\trianglelefteq G$"
prerequisites:
  - subgroup
  - normalizer
  - conjugation
extends:
  - subgroup
related:
  - quotient-group
  - kernel
  - coset
contrasts_with: []
answers_questions:
  - "What is a normal subgroup?"
  - "How do normal subgroups relate to quotient groups?"
  - "How does the kernel of a homomorphism relate to normal subgroups?"
---

# Quick Definition
A subgroup N of G is normal, written $N \trianglelefteq G$, if $gNg^{-1} = N$ for all $g \in G$. Equivalently, N is normal iff it is the kernel of some homomorphism. Normal subgroups are exactly the subgroups for which the coset multiplication is well defined.

# Core Definition
A subgroup N of G is *normal* if every element of G normalizes N, i.e., $gNg^{-1} = N$ for all $g \in G$. The following are equivalent (Theorem 6): (1) $N \trianglelefteq G$; (2) $N_G(N) = G$; (3) $gN = Ng$ for all $g \in G$; (4) the operation $uN \cdot vN = (uv)N$ on left cosets is well defined and makes them a group; (5) $gNg^{-1} \subseteq N$ for all $g \in G$. Furthermore, N is normal iff N is the kernel of some homomorphism (Proposition 7) (Dummit & Foote, pp. 82-85).

# Prerequisites
- **Subgroup** — normal subgroups are subgroups
- **Normalizer** — $N \trianglelefteq G$ iff $N_G(N) = G$
- **Conjugation** — normality is defined via conjugation

# Key Properties
1. $\{1\}$ and G are always normal in G
2. Every subgroup of an abelian group is normal
3. Every subgroup of index 2 is normal
4. $N \trianglelefteq G$ iff N is the kernel of some homomorphism
5. $Z(G) \trianglelefteq G$ always
6. Normality is NOT transitive: $A \trianglelefteq B \trianglelefteq C$ does not imply $A \trianglelefteq C$
7. To check normality: it suffices to check conjugates of generators of N by generators of G

# Construction / Recognition
## To Identify/Recognize:
1. Show $gNg^{-1} \subseteq N$ for all $g \in G$, OR
2. Show N is the kernel of a homomorphism, OR
3. Show $|G:N| = 2$ (automatic normality), OR
4. Check conjugates of generators of N by generators of G lie in N

# Context & Application
Normal subgroups are the subgroups for which quotient groups can be formed. They are the group-theoretic analogue of ideals in ring theory. Finding normal subgroups is essential for understanding group structure through the Holder program.

# Examples
**Example 1** (p. 87): $\langle (123) \rangle \trianglelefteq S_3$ since it has index 2.
**Example 2** (p. 88): Any subgroup of index 2 is normal (e.g., $\langle r \rangle \trianglelefteq D_{2n}$).
**Example 3** (p. 88): $\langle s \rangle$ is NOT normal in $D_8$ since $rsr^{-1} = sr^{-2} \notin \langle s \rangle$.

# Relationships
## Builds Upon
- **subgroup**, **normalizer**, **conjugation**

## Enables
- **quotient-group** — $G/N$ is a group iff $N \trianglelefteq G$
- **first-isomorphism-theorem** — $G/\ker\varphi \cong \text{im}(\varphi)$

## Related
- **kernel** — kernels are normal subgroups
- **coset** — left and right cosets coincide for normal subgroups

# Common Errors
- **Error**: Checking $gng^{-1} \in N$ for specific g and n rather than all. **Correction**: Must hold for ALL $g \in G$ and ALL $n \in N$ (though generators suffice).

# Common Confusions
- **Confusion**: Thinking normality is transitive. **Clarification**: $\langle s \rangle \trianglelefteq \langle s, r^2 \rangle \trianglelefteq D_8$ but $\langle s \rangle$ is not normal in $D_8$.
- **Confusion**: Thinking normality is about N being abelian. **Clarification**: Normality is an embedding property (depends on how N sits inside G), not an intrinsic property of N.

# Source Reference
Chapter 3: Quotient Groups and Homomorphisms, Section 3.1, pages 82-90, Theorem 6, Proposition 7.

# Verification Notes
- Definition source: direct from source pp. 82-84
- Confidence rationale: central definition with multiple equivalent characterizations
- Uncertainties: none
- Cross-reference status: verified
