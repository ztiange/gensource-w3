const PptxGenJS = require("pptxgenjs");
const { warnIfSlideHasOverlaps, warnIfSlideElementsOutOfBounds } = require("./pptxgenjs_helpers");

async function generate() {
  const pptx = new PptxGenJS();
  pptx.layout = "LAYOUT_WIDE"; // 16:9
  const themeFont = "微软雅黑"; // Microsoft YaHei
  const brandColor = "0F62FE";

  // Define Slide Masters
  pptx.defineSlideMaster({
    title: "TITLE_SLIDE",
    background: { color: "FFFFFF" },
    objects: [
      {
        rect: { x: 0, y: 0, w: "100%", h: "100%", fill: { color: brandColor } }
      },
      {
        text: {
          text: "销售数据分析系统",
          options: { x: 1.0, y: 2.5, w: 11.33, h: 1.5, fontSize: 54, fontFace: themeFont, color: "FFFFFF", bold: true, align: "center" }
        }
      },
      {
        text: {
          text: "基于 Streamlit 的 Vibe Coding 示例项目",
          options: { x: 1.0, y: 4.0, w: 11.33, h: 1.0, fontSize: 32, fontFace: themeFont, color: "E0E0E0", align: "center" }
        }
      }
    ]
  });

  pptx.defineSlideMaster({
    title: "CONTENT_SLIDE",
    background: { color: "FFFFFF" },
    objects: [
      {
        rect: { x: 0, y: 0, w: "100%", h: 0.8, fill: { color: brandColor } }
      },
      {
        text: {
          text: "销售数据分析系统 - Vibe Coding 示例",
          options: { x: 0.5, y: 0.2, w: 12.0, h: 0.4, fontSize: 14, fontFace: themeFont, color: "FFFFFF", align: "right" }
        }
      }
    ]
  });

  // 1. Title Slide
  const slide1 = pptx.addSlide({ masterName: "TITLE_SLIDE" });

  // 2. Project Background
  const slide2 = pptx.addSlide({ masterName: "CONTENT_SLIDE" });
  slide2.addText("项目背景与目标", { x: 0.5, y: 0.1, w: 8.0, h: 0.6, fontSize: 28, fontFace: themeFont, color: "FFFFFF", bold: true });
  slide2.addText([
    { text: "什么是 Vibe Coding？", options: { fontSize: 24, bold: true, breakLine: true } },
    { text: "通过自然语言提示（Prompt）与 AI 结对编程，快速构建可用系统。", options: { fontSize: 20, bullet: true, breakLine: true } },
    { text: "本项目展示了如何通过模块化设计引导 AI 生成高质量代码。", options: { fontSize: 20, bullet: true, breakLine: true } },
    { text: "", options: { breakLine: true } },
    { text: "项目目标", options: { fontSize: 24, bold: true, breakLine: true } },
    { text: "读取 Excel 销售数据（包含日期、商品、销量、单价）。", options: { fontSize: 20, bullet: true, breakLine: true } },
    { text: "对数据进行加载、清洗（过滤空值、异常值）。", options: { fontSize: 20, bullet: true, breakLine: true } },
    { text: "提供统计分析与多维度的数据可视化展示。", options: { fontSize: 20, bullet: true, breakLine: true } }
  ], { x: 1.0, y: 1.5, w: 11.33, h: 5.0, fontFace: themeFont, color: "333333", valign: "top", lineSpacing: 32 });
  warnIfSlideHasOverlaps(slide2, pptx);
  warnIfSlideElementsOutOfBounds(slide2, pptx);

  // 3. Core Features
  const slide3 = pptx.addSlide({ masterName: "CONTENT_SLIDE" });
  slide3.addText("核心功能特性", { x: 0.5, y: 0.1, w: 8.0, h: 0.6, fontSize: 28, fontFace: themeFont, color: "FFFFFF", bold: true });
  
  slide3.addText("自动数据清洗\n\n校验数据格式，自动剔除无效记录（如缺失值、负销量），分离有效与无效数据供用户审查。", { shape: pptx.ShapeType.rect, x: 1.0, y: 1.5, w: 5.2, h: 2.2, fill: { color: "F4F5F7" }, line: { color: "CCCCCC" }, fontSize: 16, fontFace: themeFont, color: "333333", valign: "top", align: "left" });

  slide3.addText("多维度统计分析\n\n支持商品维度（总销量、总销售额）和时间维度（每日销售额、每日销量）的自动聚合统计。", { shape: pptx.ShapeType.rect, x: 6.8, y: 1.5, w: 5.2, h: 2.2, fill: { color: "F4F5F7" }, line: { color: "CCCCCC" }, fontSize: 16, fontFace: themeFont, color: "333333", valign: "top", align: "left" });

  slide3.addText("交互式数据可视化\n\n提供各商品销量柱状图、销售额饼图、每日趋势折线图及堆叠图，支持悬浮交互。", { shape: pptx.ShapeType.rect, x: 1.0, y: 4.2, w: 5.2, h: 2.2, fill: { color: "F4F5F7" }, line: { color: "CCCCCC" }, fontSize: 16, fontFace: themeFont, color: "333333", valign: "top", align: "left" });

  slide3.addText("一键导出\n\n支持将清洗后的有效数据、被剔除的脏数据以及各项统计结果直接下载为 CSV 文件。", { shape: pptx.ShapeType.rect, x: 6.8, y: 4.2, w: 5.2, h: 2.2, fill: { color: "F4F5F7" }, line: { color: "CCCCCC" }, fontSize: 16, fontFace: themeFont, color: "333333", valign: "top", align: "left" });
  warnIfSlideHasOverlaps(slide3, pptx);
  warnIfSlideElementsOutOfBounds(slide3, pptx);

  // 4. Tech Stack
  const slide4 = pptx.addSlide({ masterName: "CONTENT_SLIDE" });
  slide4.addText("技术栈选择", { x: 0.5, y: 0.1, w: 8.0, h: 0.6, fontSize: 28, fontFace: themeFont, color: "FFFFFF", bold: true });
  slide4.addText([
    { text: "前端与框架：Streamlit", options: { fontSize: 22, bold: true, color: brandColor, breakLine: true } },
    { text: "无需编写 HTML/JS/CSS，使用纯 Python 快速构建数据驱动的交互式 Web 应用。", options: { fontSize: 18, bullet: true, breakLine: true } },
    { text: "内置丰富组件（文件上传、表格、分栏、Tab页），极其适合内部数据工具开发。", options: { fontSize: 18, bullet: true, breakLine: true } },
    { text: "", options: { breakLine: true } },
    { text: "数据处理：Pandas & OpenPyXL", options: { fontSize: 22, bold: true, color: brandColor, breakLine: true } },
    { text: "Pandas 提供高效的 DataFrame 结构，用于数据清洗、过滤和聚合运算。", options: { fontSize: 18, bullet: true, breakLine: true } },
    { text: "OpenPyXL 作为底层引擎，支持对 Excel (.xlsx, .xls) 文件的平滑读取。", options: { fontSize: 18, bullet: true, breakLine: true } },
    { text: "", options: { breakLine: true } },
    { text: "可视化展示：Plotly", options: { fontSize: 22, bold: true, color: brandColor, breakLine: true } },
    { text: "生成美观、支持交互（缩放、悬浮提示、导出图片）的现代图表。", options: { fontSize: 18, bullet: true, breakLine: true } },
    { text: "与 Streamlit 的 `st.plotly_chart` 完美集成。", options: { fontSize: 18, bullet: true, breakLine: true } }
  ], { x: 1.0, y: 1.5, w: 11.33, h: 5.0, fontFace: themeFont, color: "333333", valign: "top", lineSpacing: 28 });
  warnIfSlideHasOverlaps(slide4, pptx);
  warnIfSlideElementsOutOfBounds(slide4, pptx);

  // 5. Architecture
  const slide5 = pptx.addSlide({ masterName: "CONTENT_SLIDE" });
  slide5.addText("架构设计与模块划分", { x: 0.5, y: 0.1, w: 8.0, h: 0.6, fontSize: 28, fontFace: themeFont, color: "FFFFFF", bold: true });
  
  // Arch diagram blocks
  const blockW = 2.4;
  const blockH = 1.2;
  const startX = 1.0;
  const startY = 2.5;
  const gapX = 0.5;

  slide5.addText("app.py\n应用入口与UI层", { shape: pptx.ShapeType.rect, x: startX, y: startY, w: blockW, h: blockH, fill: { color: "E3F2FD" }, line: { color: "2196F3" }, fontSize: 16, fontFace: themeFont, bold: true, align: "center", color: "1565C0" });

  slide5.addShape(pptx.ShapeType.rightArrow, { x: startX + blockW + 0.1, y: startY + 0.4, w: gapX - 0.2, h: 0.4, fill: { color: "B0BEC5" } });

  slide5.addText("sales_reader.py\n数据读取与清洗", { shape: pptx.ShapeType.rect, x: startX + blockW + gapX, y: startY, w: blockW, h: blockH, fill: { color: "E8F5E9" }, line: { color: "4CAF50" }, fontSize: 16, fontFace: themeFont, bold: true, align: "center", color: "2E7D32" });

  slide5.addShape(pptx.ShapeType.rightArrow, { x: startX + blockW * 2 + gapX + 0.1, y: startY + 0.4, w: gapX - 0.2, h: 0.4, fill: { color: "B0BEC5" } });

  slide5.addText("sales_statistics.py\n数据统计与聚合", { shape: pptx.ShapeType.rect, x: startX + blockW * 2 + gapX * 2, y: startY - 0.8, w: blockW, h: blockH, fill: { color: "FFF3E0" }, line: { color: "FF9800" }, fontSize: 16, fontFace: themeFont, bold: true, align: "center", color: "E65100" });

  slide5.addText("sales_visualization\n交互式图表生成", { shape: pptx.ShapeType.rect, x: startX + blockW * 2 + gapX * 2, y: startY + 0.8, w: blockW, h: blockH, fill: { color: "F3E5F5" }, line: { color: "9C27B0" }, fontSize: 16, fontFace: themeFont, bold: true, align: "center", color: "6A1B9A" });

  slide5.addText([
    { text: "高内聚、低耦合的函数式设计", options: { fontSize: 22, bold: true, color: brandColor, breakLine: true } },
    { text: "UI代码与数据处理代码严格分离，`app.py` 负责展示逻辑，其他模块提供纯函数。", options: { fontSize: 18, bullet: true, breakLine: true } },
    { text: "测试代码覆盖：为每个模块提供对应的单元测试，保障修改后快速验证（Pytest）。", options: { fontSize: 18, bullet: true, breakLine: true } }
  ], { x: 1.0, y: 4.5, w: 11.33, h: 2.0, fontFace: themeFont, color: "333333", valign: "top", lineSpacing: 24 });
  warnIfSlideHasOverlaps(slide5, pptx);
  warnIfSlideElementsOutOfBounds(slide5, pptx);

  // 6. Vibe Coding Takeaways
  const slide6 = pptx.addSlide({ masterName: "CONTENT_SLIDE" });
  slide6.addText("Vibe Coding 经验总结", { x: 0.5, y: 0.1, w: 8.0, h: 0.6, fontSize: 28, fontFace: themeFont, color: "FFFFFF", bold: true });
  slide6.addText([
    { text: "模块化是 AI 生成高质量代码的前提", options: { fontSize: 22, bold: true, color: brandColor, breakLine: true } },
    { text: "将项目拆分为独立的职责模块（读取、统计、绘图），使 AI 能更聚焦地生成和修改逻辑。", options: { fontSize: 18, bullet: true, breakLine: true } },
    { text: "", options: { breakLine: true } },
    { text: "测试驱动开发（TDD）在 AI 时代的价值", options: { fontSize: 22, bold: true, color: brandColor, breakLine: true } },
    { text: "让 AI 同步生成单元测试代码（如 tests 目录下的内容）。", options: { fontSize: 18, bullet: true, breakLine: true } },
    { text: "通过运行测试来快速验证 AI 修改的正确性，避免“黑盒修Bug”。", options: { fontSize: 18, bullet: true, breakLine: true } },
    { text: "", options: { breakLine: true } },
    { text: "快速原型与即时反馈", options: { fontSize: 22, bold: true, color: brandColor, breakLine: true } },
    { text: "Streamlit 的“保存即刷新”特性极大地加速了 Vibe Coding 体验。", options: { fontSize: 18, bullet: true, breakLine: true } },
    { text: "所见即所得，开发者可以像“指挥家”一样快速调整 Prompt 达成理想效果。", options: { fontSize: 18, bullet: true, breakLine: true } }
  ], { x: 1.0, y: 1.5, w: 11.33, h: 5.0, fontFace: themeFont, color: "333333", valign: "top", lineSpacing: 24 });
  warnIfSlideHasOverlaps(slide6, pptx);
  warnIfSlideElementsOutOfBounds(slide6, pptx);

  await pptx.writeFile({ fileName: "Sales_Data_Analysis_System.pptx" });
  console.log("Done");
}

generate().catch(console.error);
