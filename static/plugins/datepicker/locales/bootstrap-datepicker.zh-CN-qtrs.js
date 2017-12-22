/**
 * Simplified Chinese translation for bootstrap-datepicker
 * Yuan Cheung <advanimal@gmail.com>
 */
;(function($){
	$.fn.datepicker.dates['zh-CN-qtrs'] = {
		days: ["星期日", "星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"],
	    daysShort: ["周日", "周一", "周二", "周三", "周四", "周五", "周六", "周日"],
	    daysMin:  ["日", "一", "二", "三", "四", "五", "六", "日"],
	    months: ["Q1", "Q2", "Q3", "Q4", "", "", "", "", "", "", "", ""],
	    monthsShort: ["一季度", "二季度", "三季度", "四季度", "", "", "", "", "", "", "", ""],
	    clear: "清除",
	    format: "mm/dd/yyyy",
  		titleFormat: "MM yyyy",
  		today: "今天",
	    meridiem: ["上午", "下午"],
	    weekStart: 0
	};
}(jQuery));
