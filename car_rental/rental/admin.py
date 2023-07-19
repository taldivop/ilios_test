from django.contrib import admin
from car_rental.rental.models import Rental
from django.contrib import messages
from django.utils.translation import ngettext



class RentalAdmin(admin.ModelAdmin):

    list_display = ['car', 'status', 'pick_up_date', 'drop_off_date', 'created_at']
    search_fields = ['pick_up_date', 'drop_off_date']
    list_filter = ['car','pick_up_date', 'drop_off_date', 'created_at']
    list_per_page = 15
    actions = ["confirm_rental", "cancel_rental"]

    @admin.action(description="Confirmar aluguéis selecionados.")
    def confirm_rental(self, request, queryset):
        updated = queryset.update(status="1")
        self.message_user(
            request,
            ngettext(
                "%d aluguel aprovado com sucesso.",
                "%d aluguéis aprovados com sucesso.",
                updated,
            )
            % updated,
            messages.SUCCESS,
        )

    @admin.action(description="Cancelar aluguéis selecionados.")
    def cancel_rental(self, request, queryset):
        updated = queryset.update(status="2")
        self.message_user(
            request,
            ngettext(
                "%d aluguel cancelado com sucesso.",
                "%d aluguéis cancelados com sucesso.",
                updated,
            )
            % updated,
            messages.SUCCESS,
        )
        


admin.site.register(Rental, RentalAdmin)
