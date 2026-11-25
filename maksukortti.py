def test_osto_ei_onnistu_jos_saldo_ei_riita():
    kortti = Maksukortti(12.00)

    kortti.osta(12.80)

    assert kortti.saldo_euroina() == 12.00