"use strict";(self.webpackChunk_N_E=self.webpackChunk_N_E||[]).push([[8933],{18933:function(t,e,n){n.r(e);var l=n(39977),i=n(67294),a=n(44397),r=n(23408),s=n(5062),o=n(62541),c=n(55926),u=n(81452),m=n(69603),d=n(47422),x=n(82730),f=n(85713);function p(t,e){return function(t){if(Array.isArray(t))return t}(t)||function(t,e){var n=[],l=!0,i=!1,a=void 0;try{for(var r,s=t[Symbol.iterator]();!(l=(r=s.next()).done)&&(n.push(r.value),!e||n.length!==e);l=!0);}catch(o){i=!0,a=o}finally{try{l||null==s.return||s.return()}finally{if(i)throw a}}return n}(t,e)||function(){throw new TypeError("Invalid attempt to destructure non-iterable instance")}()}function g(t){return function(t){if(Array.isArray(t)){for(var e=0,n=new Array(t.length);e<t.length;e++)n[e]=t[e];return n}}(t)||function(t){if(Symbol.iterator in Object(t)||"[object Arguments]"===Object.prototype.toString.call(t))return Array.from(t)}(t)||function(){throw new TypeError("Invalid attempt to spread non-iterable instance")}()}var h=function(t){var e=t.className,n=t.style,i=t.onClick,a=t.svgClassName;return(0,l.tZ)("span",{className:e,style:n,onClick:i,children:(0,l.tZ)(s.UQ,{containerClassName:"w-full sm:max-w-12-5/100",svgClassName:(0,c.C)(["w-27px h-40px md:w-18px fill-current",a])})})},y=function(t){var e=t.className,n=t.style,i=t.onClick,a=t.svgClassName;return(0,l.tZ)("span",{className:e,style:n,onClick:i,children:(0,l.tZ)(s.t2,{containerClassName:"w-full sm:max-w-12-5/100",svgClassName:(0,c.C)(["w-27px h-40px md:w-18px fill-current",a])})})},v=function(t){var e=t.slide,n=(0,i.useMemo)((function(){var t=[];return e.surtitle&&t.push((function(t){var n=t.className;return(0,l.tZ)(o.x,{className:(0,c.C)(["sm:text-17px md:text-20px lg:text-1-5vw text-1-25vw sm:leading-21px md:leading-26px lg:leading-1-8vw leading-1-56vw",n]),html:e.surtitle})})),e.title&&t.push((function(t){var n=t.className;return(0,l.tZ)(o.x,{className:(0,c.C)(["sm:text-24px md:text-48px lg:text-3-7vw text-3vw sm:leading-31px md:leading-54px lg:leading-5vw leading-4vw",n]),html:e.title})})),e.subtitle&&t.push((function(t){var n=t.className;return(0,l.tZ)(o.x,{className:(0,c.C)(["sm:text-14px md:text-17px lg:text-1vw text-0-88vw sm:leading-18px md:leading-24px lg:leading-1-56vw leading-1-25vw mb-25px",n]),html:e.subtitle})})),e.link&&e.linkTitle&&t.push((function(t){var n=t.className;return(0,l.tZ)(f.Z,{children:(0,l.tZ)(u.Z,{layout:e.layout,className:n,fieldProps:{href:e.link,blank:e.linkBlank,title:e.linkTitle}})})})),t}),[e]);return(0,l.BX)("div",{sx:{width:"100vw"},className:"relative w-full keen-slider__slide",children:[(0,l.tZ)(r.Q,{src:e.desktopImage.src,dimensions:e.desktopImage.dimensions,mobile:e.mobileImage,alt:e.desktopImage.alt,className:"w-full object-cover h-full",loading:"eager"}),(0,l.tZ)(m.j,{layout:e.layout}),(0,l.tZ)("div",{className:"absolute top-0 w-full h-full py-5 flex justify-center",children:(0,l.tZ)("div",{className:(0,c.C)(["container mx-auto my-0 flex flex-col",e.layout.textAlign?"left"==e.layout.textAlign?"items-start":"right"==e.layout.textAlign?"items-end":"items-center text-center":"items-center text-center",e.layout.textVerticalAlign?"top"==e.layout.textVerticalAlign?"justify-start":"bottom"==e.layout.textVerticalAlign?"justify-end":"justify-center":"justify-center",e.layout.mobileTextAlign?"top"==e.layout.mobileTextAlign?"md:justify-start":"bottom"==e.layout.mobileTextAlign?"md:justify-end":"left"==e.layout.mobileTextAlign?"md:items-start":"right"==e.layout.mobileTextAlign?"md:items-end":"md:justify-center md:items-center":"md:justify-center md:items-center"]),children:(0,l.tZ)("div",{className:"sm:max-w-full md:max-w-75/100 max-w-85/100 flex flex-col",children:n.map((function(t,e){return(0,l.tZ)(t,{className:"delay-"+50*e},e)}))})})})]})};e.default=function(t){var e=t.content,n=t.layout,r=(0,d.S)(),s=(0,i.useState)(0),o=s[0],c=s[1],u=(0,i.useState)(!1),m=u[0],w=u[1],b=p((0,x.E)({initial:0,loop:!0,dragSpeed:.1,slides:{perView:1,origin:"center"},slideChanged:function(t){c(t.track.details.rel)},created:function(){w(!0)}}),2),Z=b[0],N=b[1];return(0,l.tZ)(a.td,{id:e.id,className:"flex flex-col relative w-full bg-gray max-w-full min-w-0 min-h-0",layout:n,sx:{overflowX:"hidden"},children:(0,l.BX)(f.Z,{className:"navigation-wrapper",sx:{position:"relative",display:"flex",flexDirection:"column",margin:"auto"},children:[(0,l.tZ)(f.Z,{sx:{zIndex:1,position:"absolute",width:"80px",top:0,bottom:0,display:r.width>=720?"flex":"none",justifyContent:"center",alignItems:"center"},onClick:function(t){var e;return t.stopPropagation()||(null===(e=N.current)||void 0===e?void 0:e.prev())},children:(0,l.tZ)(y,{svgClassName:"#ffffff"==n.textColor?"text-white":"text-black"})}),(0,l.tZ)(f.Z,{ref:Z,className:"keen-slider",sx:{width:0!==r.width&&"100vw !important",margin:"auto"},children:e.slides.map((function(t,e){return(0,l.tZ)(v,{slide:t},e)}))}),(0,l.tZ)(f.Z,{sx:{zIndex:1,position:"absolute",width:"80px",right:0,bottom:0,top:0,display:r.width>=720?"flex":"none",justifyContent:"center",alignItems:"center"},onClick:function(t){var e;return t.stopPropagation()||(null===(e=N.current)||void 0===e?void 0:e.next())},children:(0,l.tZ)(h,{svgClassName:"#ffffff"==n.textColor?"text-white":"text-black"})}),m&&N.current&&r.width<800&&(0,l.tZ)(f.Z,{className:"dots",sx:{position:"absolute",left:0,right:0,bottom:0,height:"fit-content",display:"flex",justifyContent:"center",alignItems:"center"},children:(0,l.tZ)("ul",{sx:{margin:"0px",display:"flex"},children:g(Array(N.current.track.details.slides.length).keys()).map((function(t){return(0,l.tZ)("li",{sx:{height:"auto !important",width:"100% !important",paddingX:"4px !important",paddingY:"4px !important",marginX:"2px !important"},children:(0,l.tZ)("button",{sx:{backgroundColor:o===t?"accent":"white",borderRadius:"50%",width:"8px",height:"8px",color:"black",outline:o!==t&&"0.5px solid black"},onClick:function(){var e;null===(e=N.current)||void 0===e||e.moveToIdx(t)}},t)},t)}))})})]})})}}}]);