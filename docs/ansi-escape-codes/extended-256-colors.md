---
title: How to Use 256 Colors in ANSI Escape Codes
description: Learn how to use the extended 8-bit VGA palette with 256 colors in terminal output using Python and ANSI escape codes. Includes color maps and code examples.
tags:
    - Documentation
    - Tutorial
    - ANSI Escape Codes
    - Extended 256 Colors
---

# Extended VGA Palette with 256 Colors in ANSI Escape Codes
## Structure
The VGA color palette was introduced with the IBM VGA display adapter in 1987. The 8-bit color space has 256 colors in total, covering:

* 216 colors in a 6x6x6 color cube of red, green, and blue
* 24 shades of gray

It works both with foreground text and background colors. Simply replace the three underscores `___` with any number from `0` to `255`:

| Code             | Placement  |
| :--------------: | :--------: |
| `\x1b[38;5;___m` | Text       |
| `\x1b[48;5;___m` | Background |

### Sequence Parts
For example, the sequences `\x1b[38;5;201m` for pink foreground text and `\x1b[48;5;201m` for pink background can be broken down into the following parts:

| Part        | `\x1b[` | `38;5;`<br>`48;5;` | `201` | `m` |
| ----------- | :-----: | :----------------: | :---: | :-: |
| Description | Starts sequence, also called the Control Sequence Introducer (CSI). | Select foreground text or background color. | Color code between 0-255. | Ends sequence and calls the graphics function Select Graphic Rendition (SGR). |

## Examples
For example, `\x1b[38;5;166m` is an orange foreground text color, and `\x1b[48;5;243m` is a light gray background color. When wrapped with `\x1b[0m` to reset the color, you can write this:

```python linenums="1"
print("This is \x1b[38;5;166mORANGE\x1b[0m text")
print("This is \x1b[48;5;243mLIGHT GRAY\x1b[0m background")
```

How it looks in the terminal:

<pre><code>% This is <span class="extended-colors" style="--fg-color: #d75f00;">ORANGE</span> text
% This is <span class="extended-colors" style="--bg-color: #767676;">LIGHT GRAY</span> background</code></pre>

## Cheat Sheets
### Standard Palette

<table>
    <tbody>
        <tr>
            <td class="extended-colors" style="--bg-color: #000000;">&nbsp;0&nbsp;</td>
            <td class="extended-colors" style="--bg-color: #800000;">&nbsp;1&nbsp;</td>
            <td class="extended-colors" style="--bg-color: #008000;">&nbsp;2&nbsp;</td>
            <td class="extended-colors" style="--bg-color: #808000;">&nbsp;3&nbsp;</td>
            <td class="extended-colors" style="--bg-color: #000080;">&nbsp;4&nbsp;</td>
            <td class="extended-colors" style="--bg-color: #800080;">&nbsp;5&nbsp;</td>
            <td class="extended-colors" style="--bg-color: #008080;">&nbsp;6&nbsp;</td>
            <td class="extended-colors" style="--bg-color: #c0c0c0;">&nbsp;7&nbsp;</td>
        </tr>
        <tr>
            <td class="extended-colors" style="--bg-color: #808080;">&nbsp;8&nbsp;</td>
            <td class="extended-colors" style="--bg-color: #ff0000;">&nbsp;9&nbsp;</td>
            <td class="extended-colors" style="--bg-color: #00ff00;">10</td>
            <td class="extended-colors" style="--bg-color: #ffff00;">11</td>
            <td class="extended-colors" style="--bg-color: #0000ff;">12</td>
            <td class="extended-colors" style="--bg-color: #ff00ff;">13</td>
            <td class="extended-colors" style="--bg-color: #00ffff;">14</td>
            <td class="extended-colors" style="--bg-color: #ffffff;">15</td>
        </tr>
    </tbody>
</table>

#### Examples
Let's use color `11` for yellow text and color `14` for cyan background:

```python linenums="1"
print("This is \x1b[38;5;11mYELLOW\x1b[0m text")
print("This is \x1b[48;5;14CYAN\x1b[0m background")
```

How it looks in the terminal:

<pre><code>% This is <span class="extended-colors" style="--fg-color: #ffff00;">YELLOW</span> text
% This is <span class="extended-colors" style="--bg-color: #00ffff;">CYAN</span> background</code></pre>

### Gray Scale

<table>
    <tbody>
        <tr>
            <td class="extended-colors" style="--bg-color: #080808;">232</td>
            <td class="extended-colors" style="--bg-color: #121212;">233</td>
            <td class="extended-colors" style="--bg-color: #1c1c1c;">234</td>
            <td class="extended-colors" style="--bg-color: #262626;">235</td>
            <td class="extended-colors" style="--bg-color: #303030;">236</td>
            <td class="extended-colors" style="--bg-color: #3a3a3a;">237</td>
            <td class="extended-colors" style="--bg-color: #444444;">238</td>
            <td class="extended-colors" style="--bg-color: #4e4e4e;">239</td>
        </tr>
        <tr>
            <td class="extended-colors" style="--bg-color: #585858;">240</td>
            <td class="extended-colors" style="--bg-color: #626262;">241</td>
            <td class="extended-colors" style="--bg-color: #6c6c6c;">242</td>
            <td class="extended-colors" style="--bg-color: #767676;">243</td>
            <td class="extended-colors" style="--bg-color: #808080;">244</td>
            <td class="extended-colors" style="--bg-color: #8a8a8a;">245</td>
            <td class="extended-colors" style="--bg-color: #949494;">246</td>
            <td class="extended-colors" style="--bg-color: #9e9e9e;">247</td>
        </tr>
        <tr>
            <td class="extended-colors" style="--bg-color: #a8a8a8;">248</td>
            <td class="extended-colors" style="--bg-color: #b2b2b2;">249</td>
            <td class="extended-colors" style="--bg-color: #bcbcbc;">250</td>
            <td class="extended-colors" style="--bg-color: #c6c6c6;">251</td>
            <td class="extended-colors" style="--bg-color: #d0d0d0;">252</td>
            <td class="extended-colors" style="--bg-color: #dadada;">253</td>
            <td class="extended-colors" style="--bg-color: #e4e4e4;">254</td>
            <td class="extended-colors" style="--bg-color: #eeeeee;">255</td>
        </tr>
        </tbody>
</table>

#### Examples
Let's use color `244` for light gray text and color `234` for dark gray background:

```python linenums="1"
print("This is \x1b[38;5;244mLIGHT GRAY\x1b[0m text")
print("This is \x1b[48;5;234mDARK GRAY\x1b[0m background")
```

How it looks in the terminal:

<pre><code>% This is <span class="extended-colors" style="--fg-color: #808080;">LIGHT GRAY</span> text
% This is <span class="extended-colors" style="--bg-color: #1c1c1c;">DARK GRAY</span> background</code></pre>

### Extended Palette

<table>
    <tbody>
        <tr>
            <td class="extended-colors" style="--bg-color: #000000;">16</td>
            <td class="extended-colors" style="--bg-color: #00005f;">17</td>
            <td class="extended-colors" style="--bg-color: #000087;">18</td>
            <td class="extended-colors" style="--bg-color: #0000af;">19</td>
            <td class="extended-colors" style="--bg-color: #0000d7;">20</td>
            <td class="extended-colors" style="--bg-color: #0000ff;">21</td>
        </tr>
        <tr>
            <td class="extended-colors" style="--bg-color: #005f00;">22</td>
            <td class="extended-colors" style="--bg-color: #005f5f;">23</td>
            <td class="extended-colors" style="--bg-color: #005f87;">24</td>
            <td class="extended-colors" style="--bg-color: #005faf;">25</td>
            <td class="extended-colors" style="--bg-color: #005fd7;">26</td>
            <td class="extended-colors" style="--bg-color: #005fff;">27</td>
        </tr>
        <tr>
            <td class="extended-colors" style="--bg-color: #008700;">28</td>
            <td class="extended-colors" style="--bg-color: #00875f;">29</td>
            <td class="extended-colors" style="--bg-color: #008787;">30</td>
            <td class="extended-colors" style="--bg-color: #0087af;">31</td>
            <td class="extended-colors" style="--bg-color: #0087d7;">32</td>
            <td class="extended-colors" style="--bg-color: #0087ff;">33</td>
        </tr>
        <tr>
            <td class="extended-colors" style="--bg-color: #00af00;">34</td>
            <td class="extended-colors" style="--bg-color: #00af5f;">35</td>
            <td class="extended-colors" style="--bg-color: #00af87;">36</td>
            <td class="extended-colors" style="--bg-color: #00afaf;">37</td>
            <td class="extended-colors" style="--bg-color: #00afd7;">38</td>
            <td class="extended-colors" style="--bg-color: #00afff;">39</td>
        </tr>
        <tr>
            <td class="extended-colors" style="--bg-color: #00d700;">40</td>
            <td class="extended-colors" style="--bg-color: #00d75f;">41</td>
            <td class="extended-colors" style="--bg-color: #00d787;">42</td>
            <td class="extended-colors" style="--bg-color: #00d7af;">43</td>
            <td class="extended-colors" style="--bg-color: #00d7d7;">44</td>
            <td class="extended-colors" style="--bg-color: #00d7ff;">45</td>
        </tr>
        <tr>
            <td class="extended-colors" style="--bg-color: #00ff00;">46</td>
            <td class="extended-colors" style="--bg-color: #00ff5f;">47</td>
            <td class="extended-colors" style="--bg-color: #00ff87;">48</td>
            <td class="extended-colors" style="--bg-color: #00ffaf;">49</td>
            <td class="extended-colors" style="--bg-color: #00ffd7;">50</td>
            <td class="extended-colors" style="--bg-color: #00ffff;">51</td>
        </tr>
        <tr>
            <td class="extended-colors" style="--bg-color: #5f0000;">52</td>
            <td class="extended-colors" style="--bg-color: #5f005f;">53</td>
            <td class="extended-colors" style="--bg-color: #5f0087;">54</td>
            <td class="extended-colors" style="--bg-color: #5f00af;">55</td>
            <td class="extended-colors" style="--bg-color: #5f00d7;">56</td>
            <td class="extended-colors" style="--bg-color: #5f00ff;">57</td>
        </tr>
        <tr>
            <td class="extended-colors" style="--bg-color: #5f5f00;">58</td>
            <td class="extended-colors" style="--bg-color: #5f5f5f;">59</td>
            <td class="extended-colors" style="--bg-color: #5f5f87;">60</td>
            <td class="extended-colors" style="--bg-color: #5f5faf;">61</td>
            <td class="extended-colors" style="--bg-color: #5f5fd7;">62</td>
            <td class="extended-colors" style="--bg-color: #5f5fff;">63</td>
        </tr>
        <tr>
            <td class="extended-colors" style="--bg-color: #5f8700;">64</td>
            <td class="extended-colors" style="--bg-color: #5f875f;">65</td>
            <td class="extended-colors" style="--bg-color: #5f8787;">66</td>
            <td class="extended-colors" style="--bg-color: #5f87af;">67</td>
            <td class="extended-colors" style="--bg-color: #5f87d7;">68</td>
            <td class="extended-colors" style="--bg-color: #5f87ff;">69</td>
        </tr>
        <tr>
            <td class="extended-colors" style="--bg-color: #5faf00;">70</td>
            <td class="extended-colors" style="--bg-color: #5faf5f;">71</td>
            <td class="extended-colors" style="--bg-color: #5faf87;">72</td>
            <td class="extended-colors" style="--bg-color: #5fafaf;">73</td>
            <td class="extended-colors" style="--bg-color: #5fafd7;">74</td>
            <td class="extended-colors" style="--bg-color: #5fafff;">75</td>
        </tr>
        <tr>
            <td class="extended-colors" style="--bg-color: #5fd700;">76</td>
            <td class="extended-colors" style="--bg-color: #5fd75f;">77</td>
            <td class="extended-colors" style="--bg-color: #5fd787;">78</td>
            <td class="extended-colors" style="--bg-color: #5fd7af;">79</td>
            <td class="extended-colors" style="--bg-color: #5fd7d7;">80</td>
            <td class="extended-colors" style="--bg-color: #5fd7ff;">81</td>
        </tr>
        <tr>
            <td class="extended-colors" style="--bg-color: #5fff00;">82</td>
            <td class="extended-colors" style="--bg-color: #5fff5f;">83</td>
            <td class="extended-colors" style="--bg-color: #5fff87;">84</td>
            <td class="extended-colors" style="--bg-color: #5fffaf;">85</td>
            <td class="extended-colors" style="--bg-color: #5fffd7;">86</td>
            <td class="extended-colors" style="--bg-color: #5fffff;">87</td>
        </tr>
        <tr>
            <td class="extended-colors" style="--bg-color: #870000;">88</td>
            <td class="extended-colors" style="--bg-color: #87005f;">89</td>
            <td class="extended-colors" style="--bg-color: #870087;">90</td>
            <td class="extended-colors" style="--bg-color: #8700af;">91</td>
            <td class="extended-colors" style="--bg-color: #8700d7;">92</td>
            <td class="extended-colors" style="--bg-color: #8700ff;">93</td>
        </tr>
        <tr>
            <td class="extended-colors" style="--bg-color: #875f00;">94</td>
            <td class="extended-colors" style="--bg-color: #875f5f;">95</td>
            <td class="extended-colors" style="--bg-color: #875f87;">96</td>
            <td class="extended-colors" style="--bg-color: #875faf;">97</td>
            <td class="extended-colors" style="--bg-color: #875fd7;">98</td>
            <td class="extended-colors" style="--bg-color: #875fff;">99</td>
        </tr>
        <tr>
            <td class="extended-colors" style="--bg-color: #878700;">100</td>
            <td class="extended-colors" style="--bg-color: #87875f;">101</td>
            <td class="extended-colors" style="--bg-color: #878787;">102</td>
            <td class="extended-colors" style="--bg-color: #8787af;">103</td>
            <td class="extended-colors" style="--bg-color: #8787d7;">104</td>
            <td class="extended-colors" style="--bg-color: #8787ff;">105</td>
        </tr>
        <tr>
            <td class="extended-colors" style="--bg-color: #87af00;">106</td>
            <td class="extended-colors" style="--bg-color: #87af5f;">107</td>
            <td class="extended-colors" style="--bg-color: #87af87;">108</td>
            <td class="extended-colors" style="--bg-color: #87afaf;">109</td>
            <td class="extended-colors" style="--bg-color: #87afd7;">110</td>
            <td class="extended-colors" style="--bg-color: #87afff;">111</td>
        </tr>
        <tr>
            <td class="extended-colors" style="--bg-color: #87d700;">112</td>
            <td class="extended-colors" style="--bg-color: #87d75f;">113</td>
            <td class="extended-colors" style="--bg-color: #87d787;">114</td>
            <td class="extended-colors" style="--bg-color: #87d7af;">115</td>
            <td class="extended-colors" style="--bg-color: #87d7d7;">116</td>
            <td class="extended-colors" style="--bg-color: #87d7ff;">117</td>
        </tr>
        <tr>
            <td class="extended-colors" style="--bg-color: #87ff00;">118</td>
            <td class="extended-colors" style="--bg-color: #87ff5f;">119</td>
            <td class="extended-colors" style="--bg-color: #87ff87;">120</td>
            <td class="extended-colors" style="--bg-color: #87ffaf;">121</td>
            <td class="extended-colors" style="--bg-color: #87ffd7;">122</td>
            <td class="extended-colors" style="--bg-color: #87ffff;">123</td>
        </tr>
        <tr>
            <td class="extended-colors" style="--bg-color: #af0000;">124</td>
            <td class="extended-colors" style="--bg-color: #af005f;">125</td>
            <td class="extended-colors" style="--bg-color: #af0087;">126</td>
            <td class="extended-colors" style="--bg-color: #af00af;">127</td>
            <td class="extended-colors" style="--bg-color: #af00d7;">128</td>
            <td class="extended-colors" style="--bg-color: #af00ff;">129</td>
        </tr>
        <tr>
            <td class="extended-colors" style="--bg-color: #af5f00;">130</td>
            <td class="extended-colors" style="--bg-color: #af5f5f;">131</td>
            <td class="extended-colors" style="--bg-color: #af5f87;">132</td>
            <td class="extended-colors" style="--bg-color: #af5faf;">133</td>
            <td class="extended-colors" style="--bg-color: #af5fd7;">134</td>
            <td class="extended-colors" style="--bg-color: #af5fff;">135</td>
        </tr>
        <tr>
            <td class="extended-colors" style="--bg-color: #af8700;">136</td>
            <td class="extended-colors" style="--bg-color: #af875f;">137</td>
            <td class="extended-colors" style="--bg-color: #af8787;">138</td>
            <td class="extended-colors" style="--bg-color: #af87af;">139</td>
            <td class="extended-colors" style="--bg-color: #af87d7;">140</td>
            <td class="extended-colors" style="--bg-color: #af87ff;">141</td>
        </tr>
        <tr>
            <td class="extended-colors" style="--bg-color: #afaf00;">142</td>
            <td class="extended-colors" style="--bg-color: #afaf5f;">143</td>
            <td class="extended-colors" style="--bg-color: #afaf87;">144</td>
            <td class="extended-colors" style="--bg-color: #afafaf;">145</td>
            <td class="extended-colors" style="--bg-color: #afafd7;">146</td>
            <td class="extended-colors" style="--bg-color: #afafff;">147</td>
        </tr>
        <tr>
            <td class="extended-colors" style="--bg-color: #afd700;">148</td>
            <td class="extended-colors" style="--bg-color: #afd75f;">149</td>
            <td class="extended-colors" style="--bg-color: #afd787;">150</td>
            <td class="extended-colors" style="--bg-color: #afd7af;">151</td>
            <td class="extended-colors" style="--bg-color: #afd7d7;">152</td>
            <td class="extended-colors" style="--bg-color: #afd7ff;">153</td>
        </tr>
        <tr>
            <td class="extended-colors" style="--bg-color: #afff00;">154</td>
            <td class="extended-colors" style="--bg-color: #afff5f;">155</td>
            <td class="extended-colors" style="--bg-color: #afff87;">156</td>
            <td class="extended-colors" style="--bg-color: #afffaf;">157</td>
            <td class="extended-colors" style="--bg-color: #afffd7;">158</td>
            <td class="extended-colors" style="--bg-color: #afffff;">159</td>
        </tr>
        <tr>
            <td class="extended-colors" style="--bg-color: #d70000;">160</td>
            <td class="extended-colors" style="--bg-color: #d7005f;">161</td>
            <td class="extended-colors" style="--bg-color: #d70087;">162</td>
            <td class="extended-colors" style="--bg-color: #d700af;">163</td>
            <td class="extended-colors" style="--bg-color: #d700d7;">164</td>
            <td class="extended-colors" style="--bg-color: #d700ff;">165</td>
        </tr>
        <tr>
            <td class="extended-colors" style="--bg-color: #d75f00;">166</td>
            <td class="extended-colors" style="--bg-color: #d75f5f;">167</td>
            <td class="extended-colors" style="--bg-color: #d75f87;">168</td>
            <td class="extended-colors" style="--bg-color: #d75faf;">169</td>
            <td class="extended-colors" style="--bg-color: #d75fd7;">170</td>
            <td class="extended-colors" style="--bg-color: #d75fff;">171</td>
        </tr>
        <tr>
            <td class="extended-colors" style="--bg-color: #d78700;">172</td>
            <td class="extended-colors" style="--bg-color: #d7875f;">173</td>
            <td class="extended-colors" style="--bg-color: #d78787;">174</td>
            <td class="extended-colors" style="--bg-color: #d787af;">175</td>
            <td class="extended-colors" style="--bg-color: #d787d7;">176</td>
            <td class="extended-colors" style="--bg-color: #d787ff;">177</td>
        </tr>
        <tr>
            <td class="extended-colors" style="--bg-color: #dfaf00;">178</td>
            <td class="extended-colors" style="--bg-color: #dfaf5f;">179</td>
            <td class="extended-colors" style="--bg-color: #dfaf87;">180</td>
            <td class="extended-colors" style="--bg-color: #dfafaf;">181</td>
            <td class="extended-colors" style="--bg-color: #dfafdf;">182</td>
            <td class="extended-colors" style="--bg-color: #dfafff;">183</td>
        </tr>
        <tr>
            <td class="extended-colors" style="--bg-color: #dfdf00;">184</td>
            <td class="extended-colors" style="--bg-color: #dfdf5f;">185</td>
            <td class="extended-colors" style="--bg-color: #dfdf87;">186</td>
            <td class="extended-colors" style="--bg-color: #dfdfaf;">187</td>
            <td class="extended-colors" style="--bg-color: #dfdfdf;">188</td>
            <td class="extended-colors" style="--bg-color: #dfdfff;">189</td>
        </tr>
        <tr>
            <td class="extended-colors" style="--bg-color: #dfff00;">190</td>
            <td class="extended-colors" style="--bg-color: #dfff5f;">191</td>
            <td class="extended-colors" style="--bg-color: #dfff87;">192</td>
            <td class="extended-colors" style="--bg-color: #dfffaf;">193</td>
            <td class="extended-colors" style="--bg-color: #dfffdf;">194</td>
            <td class="extended-colors" style="--bg-color: #dfffff;">195</td>
        </tr>
        <tr>
            <td class="extended-colors" style="--bg-color: #ff0000;">196</td>
            <td class="extended-colors" style="--bg-color: #ff005f;">197</td>
            <td class="extended-colors" style="--bg-color: #ff0087;">198</td>
            <td class="extended-colors" style="--bg-color: #ff00af;">199</td>
            <td class="extended-colors" style="--bg-color: #ff00df;">200</td>
            <td class="extended-colors" style="--bg-color: #ff00ff;">201</td>
        </tr>
        <tr>
            <td class="extended-colors" style="--bg-color: #ff5f00;">202</td>
            <td class="extended-colors" style="--bg-color: #ff5f5f;">203</td>
            <td class="extended-colors" style="--bg-color: #ff5f87;">204</td>
            <td class="extended-colors" style="--bg-color: #ff5faf;">205</td>
            <td class="extended-colors" style="--bg-color: #ff5fdf;">206</td>
            <td class="extended-colors" style="--bg-color: #ff5fff;">207</td>
        </tr>
        <tr>
            <td class="extended-colors" style="--bg-color: #ff8700;">208</td>
            <td class="extended-colors" style="--bg-color: #ff875f;">209</td>
            <td class="extended-colors" style="--bg-color: #ff8787;">210</td>
            <td class="extended-colors" style="--bg-color: #ff87af;">211</td>
            <td class="extended-colors" style="--bg-color: #ff87df;">212</td>
            <td class="extended-colors" style="--bg-color: #ff87ff;">213</td>
        </tr>
        <tr>
            <td class="extended-colors" style="--bg-color: #ffaf00;">214</td>
            <td class="extended-colors" style="--bg-color: #ffaf5f;">215</td>
            <td class="extended-colors" style="--bg-color: #ffaf87;">216</td>
            <td class="extended-colors" style="--bg-color: #ffafaf;">217</td>
            <td class="extended-colors" style="--bg-color: #ffafdf;">218</td>
            <td class="extended-colors" style="--bg-color: #ffafff;">219</td>
        </tr>
        <tr>
            <td class="extended-colors" style="--bg-color: #ffdf00;">220</td>
            <td class="extended-colors" style="--bg-color: #ffdf5f;">221</td>
            <td class="extended-colors" style="--bg-color: #ffdf87;">222</td>
            <td class="extended-colors" style="--bg-color: #ffdfaf;">223</td>
            <td class="extended-colors" style="--bg-color: #ffdfdf;">224</td>
            <td class="extended-colors" style="--bg-color: #ffdfff;">225</td>
        </tr>
        <tr>
            <td class="extended-colors" style="--bg-color: #ffff00;">226</td>
            <td class="extended-colors" style="--bg-color: #ffff5f;">227</td>
            <td class="extended-colors" style="--bg-color: #ffff87;">228</td>
            <td class="extended-colors" style="--bg-color: #ffffaf;">229</td>
            <td class="extended-colors" style="--bg-color: #ffffdf;">230</td>
            <td class="extended-colors" style="--bg-color: #ffffff;">231</td>
        </tr>
    </tbody>
</table>

#### Examples
Let's use color `19` for royal blue text and color `201` for pink background:

```python linenums="1"
print("This is \x1b[38;5;19mROYAL BLUE\x1b[0m text")
print("This is \x1b[48;5;201mPINK\x1b[0m background")
```

How it looks in the terminal:

<pre><code>% This is <span class="extended-colors" style="--fg-color: #0000af;">ROYAL BLUE</span> text
% This is <span class="extended-colors" style="--bg-color: #ff00ff;">PINK</span> background</code></pre>
