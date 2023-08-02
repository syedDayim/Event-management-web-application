from django import forms
from django.contrib import admin
from django.shortcuts import render, redirect
from .models import Paper

class PercentageForm(forms.Form):
    percentage = forms.IntegerField(label="Percentage")

class PaperAdmin(admin.ModelAdmin):
    list_display = ('title', 'pdf', 'user', 'percentage')
    actions = ['assign_percentages']

    def assign_percentages(self, request, queryset):
        print("Inside assign_percentages")
        form = PercentageForm(request.POST)
        print("Form submitted")
        print("Form details saved")    
            
        if form.is_valid():
            print("Form is valid")
            percentage = form.cleaned_data['percentage']
            print(f"Percentage value: {percentage}")
                
            for paper in queryset:
                paper.percentage = percentage
                paper.save()
            print("Form details saved")    
            self.message_user(request, f"Percentages assigned: {percentage}%")
            return redirect('admin:papers_paper_changelist')

        form = PercentageForm()
        return self.display_form(request, form, queryset)

    assign_percentages.short_description = "Assign Percentages to Selected Papers"

    def display_form(self, request, form, queryset):
        opts = self.model._meta
        app_label = opts.app_label
        return render(request, 'admin/papers/assign_percentages_form.html', context={
            'title': "Assign percentages to selected papers",
            'action': 'assign_percentages',
            'opts': opts,
            'app_label': app_label,
            'queryset': queryset,
            'form': form,
        })

admin.site.register(Paper, PaperAdmin)
