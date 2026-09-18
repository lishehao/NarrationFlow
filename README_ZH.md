# NarrationFlow 1.8.1-rc.1

NarrationFlow 是一套**旁白优先、视觉对象语义化、Attention 与语言对齐、插件可热插拔**的讲解视频生产系统。

核心结构：

```text
事实与旁白
→ 实际音频与 cue
→ 场景插件注册语义对象
→ 统一 Attention Layer 决定指向、点击、划线和显隐
→ Renderer 执行或跨平台交接
```

## 当前视觉方向

默认使用 **Light Keynote / Minimal Teaching**：
- 白色或浅暖灰背景；
- 强排版、低 chrome；
- 每页一个主焦点；
- 渐进式 reveal；
- 通过 Cursor / Pen / Spotlight / Focus Transfer 引导视线；
- 默认去掉深色科技网格、发光圆圈、随机粒子和无意义持续运镜。

## 人类化教学光标

支持：
- 曲线路径移动；
- 到达后的短暂停顿；
- 单次点击与 ripple；
- pen-tip 下划线、圈选和路径追踪；
- fractional-frame 求值；
- seek-safe 回看；
- 无随机抖动、无常驻漂浮。

Scrimba 公开说明了 live-rendered slide、语义对象和随旁白移动的 pointer，但没有公开其具体动画库、曲线或导出帧率。因此这里实现的是兼容的教学交互模型，不声称复刻其私有源码。

## Canva 热插拔

Canva 可以作为 `template_source`：
- 搜索模板和 Brand Kit；
- 生成或读取 presentation shell；
- 提取页面结构、字体、背景、卡片和视觉风格。

Canva 不负责旁白计时，也不拥有 Attention。没有导出/物化能力时，只能作为远程样式参考；有本地文件、SHA-256 和 receipt 后，slide pixels 才能进入 Renderer。

## 跨 thread 恢复

新 thread 优先读取：

```text
BOOTSTRAP.md
latest.json
releases/<version>/SKILL.md
releases/<version>/SYNC_CONTEXT.md
```

详细状态见 `IMPLEMENTATION_STATUS.md`、`CHECKS.md` 和 `references/`。
