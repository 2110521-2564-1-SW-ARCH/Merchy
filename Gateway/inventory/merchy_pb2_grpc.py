# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import merchy_pb2 as merchy__pb2


class InventoryServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetAllEntries = channel.unary_unary(
                '/InventoryService/GetAllEntries',
                request_serializer=merchy__pb2.Empty.SerializeToString,
                response_deserializer=merchy__pb2.EntryList.FromString,
                )
        self.GetEntry = channel.unary_unary(
                '/InventoryService/GetEntry',
                request_serializer=merchy__pb2.EntryId.SerializeToString,
                response_deserializer=merchy__pb2.Entry.FromString,
                )
        self.CreateEntry = channel.unary_unary(
                '/InventoryService/CreateEntry',
                request_serializer=merchy__pb2.Entry.SerializeToString,
                response_deserializer=merchy__pb2.Entry.FromString,
                )
        self.UpdateEntry = channel.unary_unary(
                '/InventoryService/UpdateEntry',
                request_serializer=merchy__pb2.Entry.SerializeToString,
                response_deserializer=merchy__pb2.Entry.FromString,
                )
        self.DeleteEntry = channel.unary_unary(
                '/InventoryService/DeleteEntry',
                request_serializer=merchy__pb2.EntryId.SerializeToString,
                response_deserializer=merchy__pb2.Empty.FromString,
                )
        self.GetAllItems = channel.unary_unary(
                '/InventoryService/GetAllItems',
                request_serializer=merchy__pb2.Empty.SerializeToString,
                response_deserializer=merchy__pb2.ItemList.FromString,
                )
        self.GetItem = channel.unary_unary(
                '/InventoryService/GetItem',
                request_serializer=merchy__pb2.ItemId.SerializeToString,
                response_deserializer=merchy__pb2.Item.FromString,
                )
        self.CreateItem = channel.unary_unary(
                '/InventoryService/CreateItem',
                request_serializer=merchy__pb2.Item.SerializeToString,
                response_deserializer=merchy__pb2.Item.FromString,
                )
        self.UpdateItem = channel.unary_unary(
                '/InventoryService/UpdateItem',
                request_serializer=merchy__pb2.Item.SerializeToString,
                response_deserializer=merchy__pb2.Item.FromString,
                )
        self.DeleteItem = channel.unary_unary(
                '/InventoryService/DeleteItem',
                request_serializer=merchy__pb2.ItemId.SerializeToString,
                response_deserializer=merchy__pb2.Empty.FromString,
                )


class InventoryServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetAllEntries(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetEntry(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateEntry(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateEntry(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteEntry(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAllItems(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetItem(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateItem(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateItem(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteItem(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_InventoryServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetAllEntries': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAllEntries,
                    request_deserializer=merchy__pb2.Empty.FromString,
                    response_serializer=merchy__pb2.EntryList.SerializeToString,
            ),
            'GetEntry': grpc.unary_unary_rpc_method_handler(
                    servicer.GetEntry,
                    request_deserializer=merchy__pb2.EntryId.FromString,
                    response_serializer=merchy__pb2.Entry.SerializeToString,
            ),
            'CreateEntry': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateEntry,
                    request_deserializer=merchy__pb2.Entry.FromString,
                    response_serializer=merchy__pb2.Entry.SerializeToString,
            ),
            'UpdateEntry': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateEntry,
                    request_deserializer=merchy__pb2.Entry.FromString,
                    response_serializer=merchy__pb2.Entry.SerializeToString,
            ),
            'DeleteEntry': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteEntry,
                    request_deserializer=merchy__pb2.EntryId.FromString,
                    response_serializer=merchy__pb2.Empty.SerializeToString,
            ),
            'GetAllItems': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAllItems,
                    request_deserializer=merchy__pb2.Empty.FromString,
                    response_serializer=merchy__pb2.ItemList.SerializeToString,
            ),
            'GetItem': grpc.unary_unary_rpc_method_handler(
                    servicer.GetItem,
                    request_deserializer=merchy__pb2.ItemId.FromString,
                    response_serializer=merchy__pb2.Item.SerializeToString,
            ),
            'CreateItem': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateItem,
                    request_deserializer=merchy__pb2.Item.FromString,
                    response_serializer=merchy__pb2.Item.SerializeToString,
            ),
            'UpdateItem': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateItem,
                    request_deserializer=merchy__pb2.Item.FromString,
                    response_serializer=merchy__pb2.Item.SerializeToString,
            ),
            'DeleteItem': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteItem,
                    request_deserializer=merchy__pb2.ItemId.FromString,
                    response_serializer=merchy__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'InventoryService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class InventoryService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetAllEntries(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/InventoryService/GetAllEntries',
            merchy__pb2.Empty.SerializeToString,
            merchy__pb2.EntryList.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetEntry(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/InventoryService/GetEntry',
            merchy__pb2.EntryId.SerializeToString,
            merchy__pb2.Entry.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateEntry(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/InventoryService/CreateEntry',
            merchy__pb2.Entry.SerializeToString,
            merchy__pb2.Entry.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateEntry(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/InventoryService/UpdateEntry',
            merchy__pb2.Entry.SerializeToString,
            merchy__pb2.Entry.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteEntry(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/InventoryService/DeleteEntry',
            merchy__pb2.EntryId.SerializeToString,
            merchy__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAllItems(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/InventoryService/GetAllItems',
            merchy__pb2.Empty.SerializeToString,
            merchy__pb2.ItemList.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetItem(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/InventoryService/GetItem',
            merchy__pb2.ItemId.SerializeToString,
            merchy__pb2.Item.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateItem(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/InventoryService/CreateItem',
            merchy__pb2.Item.SerializeToString,
            merchy__pb2.Item.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateItem(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/InventoryService/UpdateItem',
            merchy__pb2.Item.SerializeToString,
            merchy__pb2.Item.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteItem(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/InventoryService/DeleteItem',
            merchy__pb2.ItemId.SerializeToString,
            merchy__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
