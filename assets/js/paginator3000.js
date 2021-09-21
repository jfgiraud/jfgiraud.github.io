        }
        
		// drag scroll thumb event	
		$(html.scrollThumb).bind('mousedown', function(e){
			var dx = e.pageX - html.scrollThumb.xPos;
					
			$(document).bind('mousemove', function(e){
				html.scrollThumb.xPos = options.returnOrder ? e.pageX - dx : e.pageX - dx;
				draw();
			});
				
			$(document).bind('mouseup', function(){
				$(document).unbind('mousemove');
				enableSelection(html.holder);
			});
			
			disableSelection(html.holder);
		});
        
        // scroll bar click
        $(html.scrollBar).add(html.pageCurrentMark).bind('click', function (e){
            html.scrollThumb.xPos = e.pageX - $(html.scrollBar).offset().left - Math.ceil(html.scrollThumb.width()/2);
            moveScrollThumb();
            draw();   
        });
        
		// keyboard navigation event
		if (options.events.keyboard){
            $(document).keydown(function (e){					
				if (e.ctrlKey){
					switch (e.keyCode ? e.keyCode : e.which ? e.which : null){
						case 0x25:	// previous page
							el = $(options.returnOrder ? '.right.top a' : '.left.top a', html.holder);
							$.isFunction(options.clickHandler) ? el.click() : document.location.href = el.attr('href');
							break;
							  
						case 0x27:	// next page
							el = $(options.returnOrder ? '.left.top a'  : '.right.top a', html.holder);  
							$.isFunction(options.clickHandler) ? el.click() : document.location.href = el.attr('href');
							break;
					}
				}
			});   
		}
			
		// scroll navigation event
		if (options.events.scroll){
            $(html.holder).bind('mousewheel', function (e){
				html.scrollThumb.xPos += (e.delta * (options.returnOrder ? -1 : 1)) * (html.table.workWidth/options.pagesTotal);
                draw(); 
				return false;
			});	 
		}
   };
})(jQuery);
