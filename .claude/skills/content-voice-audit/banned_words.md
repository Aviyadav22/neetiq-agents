# Banned Words — NeetiQ Voice Audit

Case-insensitive, whole-word match. Any hit in any draft = flag.

## Tier A: Instant reject (AI-tells)
1. leverage
2. landscape
3. navigate (as verb in abstract sense)
4. harness
5. delve
6. realm
7. fostering / foster
8. seamless
9. empower
10. unleash
11. unlock (metaphorical)
12. dive (deep dive)
13. robust
14. streamline
15. revolutionize / revolutionary
16. groundbreaking
17. game-changing / game-changer
18. paradigm shift
19. synergy / synergies
20. ecosystem (unless describing nature or a literal tech ecosystem)
21. holistic
22. cutting-edge
23. bleeding-edge
24. state-of-the-art
25. world-class
26. best-in-class
27. next-generation / next-gen
28. thought leader / thought leadership (in first person)
29. game-changer
30. disruptive (unless quoting someone)
31. elevate (metaphorical)
32. journey (metaphorical, "my journey")
33. transformative
34. meaningful (as filler)
35. actionable
36. impactful

## Tier B: Buzzwords (reject unless technically literal)
37. optimize / optimization (OK in code context)
38. enhance
39. facilitate
40. utilize (say "use")
41. endeavor (say "try")
42. comprehensive
43. scalable (OK in code context)
44. iterate (OK in code context)
45. pivot (unless about business model)
46. ideate
47. circle back
48. touch base
49. reach out (generic; "message" / "DM" / "email" OK)
50. align / alignment (bureaucratic)
51. bandwidth (time capacity)
52. deep dive
53. low-hanging fruit
54. move the needle
55. paradigm
56. ecosystem
57. stakeholder (use "customer" or the specific role)
58. end-to-end (buzzword version)

## Tier C: AI-tells in opening or closing
59. In today's
60. In the world of
61. In the realm of
62. I'm thrilled
63. Excited to announce
64. Proud to share
65. It's with great pleasure
66. Here's the thing:
67. Let me be clear:
68. Let that sink in
69. The truth is,
70. Here's what I learned:
71. What do you think? (as closing CTA)
72. Thoughts? (as closing)
73. Agree? (as closing)
74. Let's connect (generic closing)
75. DM me (generic closing)

## Tier D: Adverbs and fillers AI overuses
76. genuinely
77. honestly
78. straightforward
79. fundamentally
80. ultimately
81. essentially
82. basically (overused)
83. truly
84. literally (when not literal)
85. incredibly
86. massively
87. absolutely
88. certainly

## Tier E: LinkedIn clichés
89. "Not just X, it's Y"
90. "More than just"
91. "Today, I'm sharing"
92. "Hot take:"
93. "Unpopular opinion:"
94. "Building in public"
95. "Quick update:"
96. "Big news!"
97. "Mind blown"
98. "This is why"
99. "Buckle up"
100. "Let's unpack this"
101. "Plot twist:"
102. "Spoiler alert:"
103. "TL;DR:"
104. "PSA:"

## Tier F: Product claims Avi would never write
105. "AI-powered" (every AI tool is AI-powered)
106. "intelligent solution"
107. "innovative platform"
108. "first-of-its-kind"
109. "one-stop shop"

## Notes

- Whole-word match. "leverages" flags on "leverage". "harnessing" flags on "harness".
- Technical contexts exempt where explicitly marked (OK in code / API docs). Social posts = no exemption.
- Direct quotes from sources get a pass if attributed.
- When a word is flagged, propose a rewrite that keeps the meaning but sounds like Avi (see `brand_identity.md` Voice DOs).
