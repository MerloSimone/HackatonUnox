"use strict";(self.webpackChunk_N_E=self.webpackChunk_N_E||[]).push([[9740],{19740:function(t,e,n){n.r(e);var i=n(39977),o=n(67294),r=n(62541),a=n(23408),l=n(55926),c=n(69603),s=n(62622),d=n(82730),m=n(85713);function u(t,e,n){return e in t?Object.defineProperty(t,e,{value:n,enumerable:!0,configurable:!0,writable:!0}):t[e]=n,t}function p(t){for(var e=1;e<arguments.length;e++){var n=null!=arguments[e]?arguments[e]:{},i=Object.keys(n);"function"===typeof Object.getOwnPropertySymbols&&(i=i.concat(Object.getOwnPropertySymbols(n).filter((function(t){return Object.getOwnPropertyDescriptor(n,t).enumerable})))),i.forEach((function(e){u(t,e,n[e])}))}return t}function f(t,e){return function(t){if(Array.isArray(t))return t}(t)||function(t,e){var n=[],i=!0,o=!1,r=void 0;try{for(var a,l=t[Symbol.iterator]();!(i=(a=l.next()).done)&&(n.push(a.value),!e||n.length!==e);i=!0);}catch(c){o=!0,r=c}finally{try{i||null==l.return||l.return()}finally{if(o)throw r}}return n}(t,e)||function(){throw new TypeError("Invalid attempt to destructure non-iterable instance")}()}function x(t){return function(t){if(Array.isArray(t)){for(var e=0,n=new Array(t.length);e<t.length;e++)n[e]=t[e];return n}}(t)||function(t){if(Symbol.iterator in Object(t)||"[object Arguments]"===Object.prototype.toString.call(t))return Array.from(t)}(t)||function(){throw new TypeError("Invalid attempt to spread non-iterable instance")}()}var b=function(t){var e,n,o=t.slide,d=t.slideIndex,m=o.layout.textAlign?o.layout.textAlign:"center";return(0,i.tZ)("a",{className:"keen-slider__slide",sx:{minWidth:"100% !important"},href:null===(e=o.firstLink)||void 0===e?void 0:e.href,target:(null===(n=o.firstLink)||void 0===n?void 0:n.blank)?"_blank":void 0,onDragStart:function(t){return t.preventDefault()},children:(0,i.BX)("div",{className:"relative md:h-w-screen h-screen",children:[(0,i.tZ)("div",{className:"absolute top-0 left-0 right-0 bottom-0",children:(0,i.tZ)(a.Q,{alt:o.desktopImage.alt,src:o.desktopImage.src,dimensions:o.desktopImage.dimensions,mobile:o.mobileImage,style:{objectFit:"cover",height:"100%",width:"100%"},loading:0===d?"eager":"lazy"})}),(0,i.tZ)(c.j,{layout:o.layout}),(0,i.tZ)("div",{className:"absolute top-0 w-full h-full py-5 flex justify-center",children:(0,i.BX)("div",{className:(0,l.C)(["container mx-auto my-0 flex flex-col",o.layout.textAlign?"right"==o.layout.textAlign?"items-end text-right":"center"==o.layout.textAlign?"items-center":"items-start":"items-start",o.layout.textVerticalAlign?"top"==o.layout.textVerticalAlign?"justify-start":"bottom"==o.layout.textVerticalAlign?"justify-end":"justify-center":"justify-center"]),children:[o.surtitle&&(0,i.tZ)(r.x,{sx:p({},(0,s.o)(["text.labelMedium"],["text.labelLarge"],["text.labelLarge"],["text.labelXLarge"])),className:(0,l.C)(["center"==m?"slideTextFadeIn text-center":"left"==m?"slideTextFadeInFromLeft":"slideTextFadeInFromRight"]),style:{animationDuration:"1.5s"},html:o.surtitle}),o.title&&(0,i.tZ)(r.x,{sx:p({},(0,s.o)(["text.displaySmall"],["text.displayMedium"],["text.displayMedium"],["text.displayLarge"])),className:(0,l.C)(["center"==m?"slideTextFadeIn text-center":"left"==m?"slideTextFadeInFromLeft":"slideTextFadeInFromRight"]),style:{animationDuration:"2s"},html:o.title}),o.subtitle&&(0,i.tZ)(r.x,{sx:p({},(0,s.o)(["text.paragraphSmall"],["text.paragraphMedium"],["text.paragraphMedium"],["text.paragraphLarge"])),className:(0,l.C)(["center"==m?"slideTextFadeIn text-center":"left"==m?"slideTextFadeInFromLeft":"slideTextFadeInFromRight"]),style:{animationDuration:"1.5s"},html:o.subtitle})]})})]})})};e.default=function(t){var e=t.content,n=t.layout,r=t.indexInPage,a=(0,o.useState)(0),c=a[0],s=a[1],u=(0,o.useState)(!1),p=u[0],h=u[1],g=f((0,d.E)({defaultAnimation:{duration:1500},initial:0,dragSpeed:.3,loop:!0,slides:{perView:1,origin:"center"},slideChanged:function(t){s(t.track.details.rel)},created:function(){h(!0)}},[function(t){var e,n=function(){clearTimeout(e),i||(e=setTimeout((function(){t.next()}),6e3))},i=!1;t.on("created",(function(){n()})),t.on("dragStarted",(function(){clearTimeout(e)})),t.on("animationEnded",n),t.on("updated",n)}]),2),y=g[0],v=g[1];return(0,i.BX)("section",{id:e.id,className:"relative band w-full ".concat(n.viewport&&1==n.viewport.length&&"desktop"==n.viewport[0]?"sm:hidden":n.viewport&&1==n.viewport.length&&"mobile"==n.viewport[0]?"sm:block hidden":""),style:{padding:0,color:n.textColor||"#fff"},children:[(n.top||n.bottom||n.left||n.right||n.topMobile||n.bottomMobile)&&(0,i.tZ)("style",{dangerouslySetInnerHTML:{__html:"\n              ".concat(n.top||n.bottom||n.left||n.right?"@media (min-width: 45em) {\n                  section#".concat(e.id," { \n                    ").concat(n.top?"margin-top: ".concat(n.top,"px !important;"):"","\n                    ").concat(n.bottom?"margin-bottom: ".concat(n.bottom,"px !important;"):"","\n                    ").concat(n.left?"padding-left: ".concat(n.left,"px !important;"):"","\n                    ").concat(n.right?"padding-right: ".concat(n.right,"px !important;"):"","\n                  }\n                }"):"","\n              ").concat(n.topMobile||n.bottomMobile?"@media (max-width: 45em) {\n                  section#".concat(e.id," { \n                    ").concat(n.topMobile?"margin-top: ".concat(n.topMobile,"px !important;"):"","\n                    ").concat(n.bottomMobile?"margin-bottom: ".concat(n.bottomMobile,"px !important;"):"","\n                  }\n                }"):"","\n              ")}}),(0,i.BX)(m.Z,{ref:y,className:"keen-slider",children:[e.slides.map((function(t,e){return(0,i.tZ)(b,{slide:t,slideIndex:0===r?e:void 0},e)})),p&&v.current&&(0,i.tZ)(m.Z,{className:"dots",sx:{position:"absolute",left:0,right:0,bottom:"24px",height:"fit-content",display:"flex",justifyContent:"center",alignItems:"center"},children:(0,i.tZ)("ul",{sx:{margin:"0px",display:"flex",paddingY:"16px"},children:x(Array(v.current.track.details.slides.length).keys()).map((function(t){return(0,i.tZ)("li",{sx:{height:"auto !important",width:"100% !important",paddingX:"4px !important",paddingY:"4px !important",marginX:"2px !important"},children:(0,i.tZ)("button",{sx:{backgroundColor:c===t?"white":"primaryB32",borderRadius:"50%",width:"8px",height:"8px",color:"black"},onClick:function(){var e;null===(e=v.current)||void 0===e||e.moveToIdx(t)}},t)},t)}))})})]}),(0,i.tZ)("section",{className:(0,l.C)(["scrolldown","absolute bottom-[15vh] left-1/2 ml-[-15px] w-[30px] h-[50px] transition-opacity transition-duration-300","max-lg:hidden md:bottom-[10vh] sm:bottom-[8vh] sm:ml-[-10px] sm:w-[20px]"]),children:(0,i.tZ)("a",{href:"#",className:"pt-[60px]",children:(0,i.tZ)("span",{className:(0,l.C)(["w-[30px] h-[50px] border-2 border-white rounded-[50px] block","sm:w-[20px] sm:h-[35px] sm:border-1 sm:rounded-[10px] sm:block","before:absolute before:top-[10px] before:left-1/2 before:w-[6px]","before:h-[6px] before:ml-[-3px] before:bg-white before:rounded-full before:animate-scroll"])})})})]})}}}]);