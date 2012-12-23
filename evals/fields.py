try:
    import south
    from south.modelsinspector import add_introspection_rules
    add_introspection_rules([], ["^social_auth\.fields\.JSONField"])
except:
    pass