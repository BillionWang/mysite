from django.template import Template,Context

for name in('John','Julie','Pat'):
	t = Template('Hello,{{name}}')
	print t.render(Context({'name':'name'}))
哈哈
