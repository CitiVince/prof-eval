<script type="text/javascript">
  $(function () {
    $('.disconnect form a').on('click', function (e) {
      e.preventDefault();
      $(this).parent('form').submit();
    });
  });
</script>